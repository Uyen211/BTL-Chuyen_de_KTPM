---
title: Order Processing Benchmark Suite (Modular Monolith vs. Microservices)
feature: experiment-suite
phase: PLAN
date: 25-11-26
complexity: COMPLEX
status: active
source_spec: docs/chuong_4_thiet_ke_thuc_nghiem.md
---

# Implementation Plan: Order Processing Benchmark Suite

## Overview, Goals, and Scope

- **Overview:** Xây dựng bộ thực nghiệm đối chứng có kiểm soát trong `experiments/` để so sánh **Modular Monolith** và **Microservices** trên cùng luồng nghiệp vụ xử lý đơn hàng (`Order`, `Inventory`, `Payment`, `Notification`), phục vụ thu thập số liệu thật cho Chương 5 và Chương 6 của báo cáo.
- **Complexity Classification:** `COMPLEX` (đa thành phần: 2 kiến trúc Java 21 / Spring Boot 3, hạ tầng Docker Compose + PostgreSQL 16 + RabbitMQ + Spring Cloud Gateway, bộ kịch bản tải `k6`, giám sát Prometheus/cAdvisor/Grafana, và script kiểm định thống kê).
- **Goals:**
  1. Đạt **Tech-stack Parity** (`Java 21`, `Spring Boot 3.x`, `PostgreSQL 16`, `HikariCP`) và **Deployment Parity** (Docker Compose).
  2. Triển khai đầy đủ cả hai luồng: *Happy Path* (`CONFIRMED`) và *Failure & Compensation Path* (`CANCELLED` qua ACID rollback ở Modular Monolith và Saga Orchestration ở Microservices).
  3. Hỗ trợ cả hai chế độ đo **`E1 – Resource Parity`** (cùng tổng trần CPU/RAM) và **`E2 – Selective Scaling`** (nhân bản riêng `payment-service` vs. nhân bản toàn bộ Modular Monolith).
  4. Tự động hóa đo đạc hiệu năng (`k6`), tài nguyên (`cAdvisor`/`docker stats`), 6 chỉ số vận hành độc lập (Mục 4.7), và kiểm định thống kê (*Shapiro-Wilk*, *Mann-Whitney U*, *Cliff's Delta*).
- **Out of Scope:** Cụm Kubernetes đa máy chủ (*multi-region cloud*), giao diện người dùng (UI), và viết nội dung Chương 5–6 (chỉ viết sau khi chạy xong benchmark và có số liệu).

---

## Touchpoints

- `experiments/modular-monolith/` — Mã nguồn ứng dụng Spring Boot 3 + Spring Modulith, `Dockerfile`, `docker-compose.e1.yml`, `docker-compose.e2.yml`.
- `experiments/microservices/` — 5 dịch vụ Spring Boot (`api-gateway`, `order-service`, `inventory-service`, `payment-service`, `notification-service`), `Dockerfile` cho từng dịch vụ, `docker-compose.e1.yml`, `docker-compose.e2.yml`.
- `experiments/k6/` — Kịch bản tải `k1_load.js`, `k2_stress.js`, `k3_spike.js`, `k4_fault_injection.js`, `k5_selective_scaling.js`.
- `experiments/monitoring/` — `prometheus.yml`, `cadvisor` config, Grafana provisioning dashboards.
- `experiments/results/` — Script chạy benchmark tự động (`run_benchmarks.ps1`), script đo chỉ số vận hành (`measure_ops.ps1`), và script thống kê Python (`analyze_results.py`).

---

## Public Contracts

Cả hai kiến trúc phải bộc lộ cùng một hợp đồng REST API tại cổng `:8080`:

1. **`POST /api/orders`**
   - Request JSON: `{"customerId": "uuid", "items": [{"productId": "uuid", "quantity": 1}], "paymentMethod": "CARD|FAIL_PAYMENT"}`
   - Response `201 Created` (*Happy Path*): `{"orderId": "uuid", "status": "CONFIRMED", "totalAmount": 100.00}`
   - Response `200 OK` hoặc `422 Unprocessable Entity` (*Compensation Path* khi `FAIL_PAYMENT` hoặc hết tồn kho): `{"orderId": "uuid", "status": "CANCELLED", "reason": "PAYMENT_FAILED|OUT_OF_STOCK"}`
2. **`GET /api/orders/{id}`**
   - Response `200 OK`: `{"orderId": "uuid", "status": "CONFIRMED|CANCELLED|PENDING", "totalAmount": 100.00, "createdAt": "..."}`
3. **`GET /actuator/health` & `/actuator/prometheus`**
   - Phục vụ kiểm tra trạng thái sẵn sàng (*healthcheck*) khi đo thời gian deploy và thu thập metrics JVM/HTTP.

---

## Blast Radius

- Toàn bộ thay đổi mã nguồn nằm cô lập trong `experiments/` — không chạm vào `docs/`, `literareview/`, `guide/`, hay `scripts/`.
- Xung đột cổng cục bộ cần kiểm soát: không chạy đồng thời `modular-monolith` và `microservices` trên cùng cổng `:8080` khi đo chế độ `E1`; kịch bản `run_benchmarks.ps1` phải `docker compose down -v` trước khi chuyển phiên bản.

---

## Implementation Checklist

1. **Khởi tạo cấu trúc & dữ liệu nền dùng chung (`experiments/db/init.sql`)**
   - Tạo script SQL khởi tạo bảng sản phẩm mẫu (1.000 SKU với tồn kho lớn để tránh nhiễu hết hàng ngoài ý muốn ở `K1`–`K3`) và bảng tài khoản khách hàng.
2. **Xây dựng phiên bản Modular Monolith (`experiments/modular-monolith/`)**
   - Khởi tạo project Maven/Gradle (`Java 21`, `Spring Boot 3.x`, `spring-modulith-starter-core`, `spring-boot-starter-data-jpa`, `spring-boot-starter-actuator`, `micrometer-registry-prometheus`).
   - Cài đặt 4 mô-đun theo package boundary: `order`, `inventory`, `payment`, `notification` (giao tiếp đồng bộ qua public service interfaces + DTOs; sự kiện `OrderCompletedEvent` qua Spring `ApplicationEventPublisher`; 4 PostgreSQL schemas tách biệt).
   - Viết `ModularityTests.java` sử dụng `ApplicationModules.of(Application.class).verify()` để xác minh không có phụ thuộc chéo/vòng trái phép.
   - Viết `Dockerfile`, `docker-compose.e1.yml` (cấp `cpus` & `mem_limit` ngang bằng tổng Microservices) và `docker-compose.e2.yml` (3 instances sau Nginx load balancer).
3. **Xây dựng phiên bản Microservices (`experiments/microservices/`)**
   - Khởi tạo 5 modules độc lập: `api-gateway` (Spring Cloud Gateway), `order-service`, `inventory-service`, `payment-service`, `notification-service` (cùng Java 21, Spring Boot 3.x, HikariCP, Actuator/Prometheus).
   - Cài đặt Saga Orchestration trong `order-service` (gọi đồng bộ `inventory-service` $\rightarrow$ `payment-service` với timeout cấu hình rõ; nếu `payment-service` lỗi thì gọi `POST /internal/inventory/release` bù trừ).
   - Cài đặt Transactional Outbox + RabbitMQ publish tới `notification-service` kèm kiểm tra `Idempotency` theo `orderId`.
   - Viết `Dockerfile` cho từng service, `docker-compose.e1.yml` (4 PostgreSQL instances + RabbitMQ + Gateway + 4 services với tổng trần app `cpus`/`mem_limit` bằng Modular Monolith) và `docker-compose.e2.yml` (scale `payment-service` lên 3 instances với Nginx/Gateway round-robin).
4. **Cấu hình giám sát & Kiểm thử tải (`experiments/monitoring/` & `experiments/k6/`)**
   - Cấu hình `prometheus.yml` scrape `/actuator/prometheus` và `cadvisor` mỗi 2 giây.
   - Viết 5 kịch bản `k6`: `k1_load.js` (20/100/250 VUs), `k2_stress.js`, `k3_spike.js`, `k4_fault_injection.js` (15% `FAIL_PAYMENT` + dừng container `payment-service`), `k5_selective_scaling.js` (Open Model `constant-arrival-rate` với độ trễ nhân tạo ở `payment`).
5. **Tự động hóa đo vận hành & Thống kê (`experiments/results/`)**
   - Viết `measure_ops.ps1` ghi nhận 6 chỉ số độc lập ở Mục 4.7: số container, số tệp/dòng YAML/env, clean build time, startup-to-healthy time, environment setup time, và log/MTTD khi tiêm lỗi.
   - Viết `run_benchmarks.ps1` chạy lặp 5–10 lượt độc lập cho từng kịch bản, thu thập JSON từ `k6` và CSV từ `docker stats`.
   - Viết `analyze_results.py` (dùng `.venv`) tính `median`, `mean`, `IQR`, kiểm định *Shapiro-Wilk*, *Mann-Whitney U*, và *Cliff's Delta* ($\delta$).

---

## Acceptance Criteria

- **AC-1 (Boundary Integrity):** `ModularityTests` xác nhận kiến trúc Modular Monolith không có vi phạm ranh giới mô-đun.
  - `proven by:` `mvn test -Dtest=ModularityTests` (`experiments/modular-monolith/`)
  - `strategy: Fully-Automated`
- **AC-2 (Functional & Saga Parity):** Cả hai hệ thống đều trả về `CONFIRMED` cho luồng hợp lệ và `CANCELLED` (kèm hoàn tác tồn kho chính xác trong DB) cho luồng `FAIL_PAYMENT`.
  - `proven by:` `integration_parity_check` (smoke test `POST /api/orders` happy & compensation paths trên cả hai stack)
  - `strategy: Fully-Automated`
- **AC-3 (Resource-Parity Enforcement):** Trong `docker-compose.e1.yml`, tổng `cpus` và `mem_limit` của các container ứng dụng ở hai kiến trúc bằng nhau chính xác.
  - `proven by:` `docker compose config` diff check
  - `strategy: Fully-Automated`
- **AC-4 (End-to-End Benchmark & Statistical Output):** Chạy thành công `k1`–`k5` ở mức pilot trên cả hai kiến trúc, xuất được dữ liệu JSON/CSV và bảng kiểm định Mann-Whitney U + Cliff's Delta.
  - `proven by:` `analyze_results.py` output summary table
  - `strategy: Hybrid`

---

## Verification Evidence

| Gate / Scenario | Strategy | Proves SPEC criterion |
| :--- | :--- | :--- |
| `ModularityTests` (`Spring Modulith`) | `Fully-Automated` | AC-1 (Ranh giới mô-đun chuẩn Chương 4.3.1) |
| Smoke test Happy & Compensation Path (`POST /api/orders`) | `Fully-Automated` | AC-2 (Hợp đồng & Saga/ACID Chương 4.2) |
| Kiểm tra `docker-compose.e1.yml` limits | `Fully-Automated` | AC-3 (Resource Parity Chương 4.1 & 4.4) |
| Pilot run `k6` (`K1`–`K5`) + `analyze_results.py` | `Hybrid` | AC-4 (Kịch bản & Thống kê Chương 4.5–4.8) |

---

## Dependencies & Risks

- **Rủi ro 1 (JVM Warm-up & GC Spikes):** JVM tiêu tốn RAM và có thể gây nhiễu độ trễ đầu phiên. *Giảm thiểu:* Bắt buộc chạy 30s *warm-up* trước mỗi lượt đo, cố định `-Xms`/`-Xmx` phù hợp với `mem_limit` của từng container, và lặp 5–10 lần.
- **Rủi ro 2 (Port & Docker Resource Contention trên 1 máy Windows):** Chạy `k6` cùng máy với Docker có thể tranh chấp CPU. *Giảm thiểu:* Giới hạn CPU cho Docker containers thấp hơn tổng số core vật lý của host để chừa tài nguyên cho `k6` và OS.
- **Rollback Safety:** Toàn bộ thử nghiệm nằm trong `experiments/` và dùng Docker volumes tạm; có thể `docker compose down -v` để khôi phục trạng thái sạch hoàn toàn bất kỳ lúc nào.

---

## Test Infra Improvement Notes
(none identified yet — sẽ cập nhật sau bước pilot run của `k6` và `cAdvisor`.)

---

## Resume and Execution Handoff

- **Next Action:** Khi người dùng xác nhận chuyển sang **EXECUTE** (Giai đoạn 5), bắt đầu từ **Checklist Step 1 & 2** (tạo `experiments/db/init.sql` và khung `experiments/modular-monolith/` trước khi nhân bản logic sang `experiments/microservices/`).
- **Authoritative Design Reference:** [docs/chuong_4_thiet_ke_thuc_nghiem.md](../../../../docs/chuong_4_thiet_ke_thuc_nghiem.md).
