# Literature Review — Nhóm 2: Thực nghiệm So sánh Hiệu năng & Tài nguyên (Monolith / Modular Monolith vs. Microservices)

Nhóm tài liệu này tổng hợp **8 nghiên cứu thực nghiệm và đánh giá hiệu năng** (từ 2015 đến 2026) đo đạc trực tiếp độ trễ, thông lượng, mức tiêu thụ CPU/RAM và chi phí hạ tầng giữa kiến trúc nguyên khối (Monolith / Modular Monolith) và Microservices. Đây là nguồn đối chứng định lượng trọng tâm cho **Chương 3 (3.1, 3.5, 3.6, 3.7)** và tham chiếu thiết kế trực tiếp cho **Chương 4**.

> [!IMPORTANT]
> Mọi số liệu dưới đây đều gắn chặt với điều kiện phần cứng, tech stack và workload của từng công trình, tuân thủ nguyên tắc không tách rời số liệu khỏi bối cảnh đo trong [huongdan.md](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/guide/huongdan.md).

| Mã tài liệu | Tác giả & Năm | Tech Stack & Môi trường | Chỉ số chính | Kết luận nổi bật |
| :--- | :--- | :--- | :--- | :--- |
| [Monolithic_vs_Microservice_Architecture_A_Performa](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-2-performance-benchmarks/md/Monolithic_vs_Microservice_Architecture_A_Performa.md) | Blinowski et al. (2022) | Java 8 (Spring Boot) & C# 8 (.NET Core), Local + Azure | Throughput, Cost-efficiency | Trên 1 máy hoặc cùng chi phí, Monolith thắng; over-scaling gây giảm hiệu năng |
| [Tail_latency_throughput_and_memory_overhead_of_mon](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-2-performance-benchmarks/md/Tail_latency_throughput_and_memory_overhead_of_mon.md) | Tofan (2026) | Node.js v18 + MariaDB 10.11, Docker giới hạn 2 CPU / 512 MB | P90/P95, Throughput, RAM, CPU | Monolith P90 thấp hơn 21–24%, throughput cao hơn 28–29%, RAM thấp hơn **3,35x** |
| [Comparative_analysis_of_selected_aspects_of_web_ap](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-2-performance-benchmarks/md/Comparative_analysis_of_selected_aspects_of_web_ap.md) | Krzysztoń et al. ($\ge 2024$) | .NET 8, PostgreSQL, MongoDB, RabbitMQ, Consul, Docker Swarm | Avg RT, Throughput | Modular Monolith + in-memory queue nhanh gấp **~3x** RabbitMQ; MS thắng ở selective scaling |
| [applsci-10-05797-v2](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-2-performance-benchmarks/md/applsci-10-05797-v2.md) | Tapia et al. (2020) | Node.js + MySQL/MongoDB; Monolith (KVM) vs. MS (Docker) | Avg RT, Throughput, Kernel `h` | MS nhanh hơn (3,1 vs 2,5 rps) nhưng bị nhiễu nặng do **KVM vs. Docker** |
| [07333476](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-2-performance-benchmarks/md/07333476.md) | Villamizar et al. (2015) | Play 2.2 (Scala/Java) + PostgreSQL trên AWS EC2/RDS | SLA RT, Chi phí/tháng | MS giảm **17%** chi phí/tháng (\$328,32 vs \$398,88) nhờ chọn VM theo tải từng service |
| [Villamizar_et_al-2017-Service_Oriented_Computing_and_Applications](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-2-performance-benchmarks/md/Villamizar_et_al-2017-Service_Oriented_Computing_and_Applications.md) | Villamizar et al. (2017) | Play/Jax-RS (EC2) vs. AWS Lambda (Node.js) + PostgreSQL | Cost/Million Req, ART | MS giảm CMR 9,5%–13,8%; Lambda giảm 50,4%–77,1%; MS có ART cao hơn do Gateway |
| [Migrating_Monolithic_to_Microservices_Comparative](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-2-performance-benchmarks/md/Migrating_Monolithic_to_Microservices_Comparative.md) | Wahyudin et al. (2025) | Monolith (**PHP Laravel**) vs. MS (**Golang gRPC**), 1 VPS 2C/8GB | Avg RT, Throughput, Error | MS vượt trội (154 ms vs 1.138 ms) nhưng bị **nhiễu hoàn toàn do khác ngôn ngữ/protocol** |
| [2305.15438v1](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-2-performance-benchmarks/md/2305.15438v1.md) | Desina (2023) | Tổng hợp 10 bài + bảng minh họa | Avg RT, CPU, Mem | Không có thực nghiệm đối chứng và thiếu baseline Monolith (giá trị thực nghiệm rất thấp) |

---

## 1. Tóm tắt chi tiết từng bài báo

### 1.1. Monolithic vs. Microservice Architecture: A Performance and Scalability Evaluation — Blinowski et al. (2022)
- **Nguồn:** `Monolithic_vs_Microservice_Architecture_A_Performa.md` (*IEEE Access*, 2022).
- **Thiết lập & Điều kiện đo:** 2 REST endpoints không dùng DB: `City` (nhẹ CPU) và `Route` (nặng CPU — heuristic TSP qua 10.000 điểm), viết trên cả **Java 8 (Spring Boot 2.3.0)** và **C# 8 (ASP.NET Core 3.1)**. Chạy JMeter (10 threads; City 1.000 req, Route 100 req, lặp 20×5 lần lấy median) trên 3 môi trường: Local (i7-9850H, 32 GB RAM), Azure Spring Cloud (1–6 instances) và Azure App Service (1–20 instances).
- **Kết quả chính:**
  - **Local:** Monolith vượt trội Microservices ở `City` (**>2x** ở .NET, **1,37x** ở Java); ở `Route` nặng CPU, Monolith chỉ nhỉnh hơn nhẹ.
  - **Azure App Service:** Vertical scaling (B1/S1 $\rightarrow$ S2) tăng throughput `City` tới **+24%** và `Route` tới **+200%** (Java); horizontal scaling 1$\rightarrow$3 và 3$\rightarrow$6 trên `Route` tăng **>100%** (tối đa 148%), nhưng tăng lên 15–20 instances gây **over-scaling** (giảm throughput).
  - **Hiệu quả chi phí:** Ở các cấu hình có cùng chi phí hạ tầng, Monolith luôn vượt trội Microservices.
- **Hạn chế:** Chỉ đo throughput (không đo latency/CPU), **không có database**, **không có giao tiếp liên dịch vụ** giữa 2 service.

---

### 1.2. Tail latency, throughput, and memory overhead of monolithic and microservices architectures in resource-constrained docker deployments — Tofan (2026)
- **Nguồn:** `Tail_latency_throughput_and_memory_overhead_of_mon.md` (Yoga Ari Tofan, 2026).
- **Thiết lập & Điều kiện đo:** Luồng `POST /orders` ghi đồng bộ với khóa dòng `SELECT ... FOR UPDATE`. Stack đồng nhất: **Node.js v18, Express v4.18.2, MariaDB 10.11**. Chạy trên AMD Ryzen 5 2400GE (14 GB RAM, Ubuntu 22.04) với **Docker resource-parity**: Monolith (`2.0 CPU / 512 MB`) vs. Microservices (`product-service 1.0 CPU / 256 MB` + `order-service 1.0 CPU / 256 MB`), DB dùng chung `0.5 CPU / 256 MB`. Đo bằng JMeter 5.6.3 qua Tailscale VPN ở 3 tải: S1 (50 users), S2 (200 users), S3 (500 users), 60s/lần, lặp 20 lần.
- **Kết quả chính (đều có ý nghĩa thống kê $p < 0{,}0001$, 0,00% lỗi):**
  - **S1 (50 users):** Monolith P90 **131,35 ms**, throughput **429,89 req/s** vs. MS P90 **171,38 ms (+30,5%)**, throughput **332,38 req/s**.
  - **S2 (200 users):** Monolith P90 **492,70 ms**, throughput **432,49 req/s** vs. MS P90 **608,11 ms**, throughput **338,07 req/s**.
  - **S3 (500 users):** Monolith P90 **1.217,60 ms**, throughput **438,25 req/s**, Peak RAM **95,31 MiB** vs. MS P90 **1.534,50 ms**, throughput **343,24 req/s**, Peak RAM **319,43 MiB (gấp 3,35x**, trong đó `order-service` chạm ~86% trần 256 MB).
- **Hạn chế:** Chỉ test 1 endpoint đồng bộ giữa 2 service; so sánh Monolith truyền thống (không phải Modular Monolith); không có API Gateway hay message broker.

---

### 1.3. Comparative analysis of selected aspects of web application architectures — Krzysztoń et al. ($\ge 2024$)
- **Nguồn:** `Comparative_analysis_of_selected_aspects_of_web_ap.md` (Lublin University of Technology).
- **Thiết lập & Điều kiện đo:** Hệ thống TMĐT (`Orders`, `Discounts`, `Products`) viết đồng nhất trên **.NET 8**, PostgreSQL 16.3, MongoDB 6.0.7, RabbitMQ 3.13.3, Consul 1.19.2, Docker Swarm trên máy AMD Ryzen 9 7945HX, 40 GB RAM, Windows 11. Đo bằng JMeter 5.6.3.
- **Kết quả chính qua 3 thí nghiệm:**
  - **Exp 1 (CRUD 1 instance):** Microservices qua API Gateway + Consul có Avg RT cao hơn Modular Monolith ở mọi thao tác: GET **+1,076 ms**, POST **+1,009 ms**, PUT **+0,605 ms**, DELETE **+0,245 ms**.
  - **Exp 2 (Giao tiếp liên thành phần, 400 threads × 250 req):** Modular Monolith + **in-memory queue** đạt **866 ms / 449 req/s** — nhanh gấp **~3x** so với Modular Monolith + RabbitMQ (**2.680 ms / 147 req/s**) và Microservices + RabbitMQ (**2.678 ms / 147 req/s**).
  - **Exp 3 (Selective scaling, 400 threads):** Modular Monolith scale 1 $\rightarrow$ 3 $\rightarrow$ 6 instances giảm RT từ **2.637 $\rightarrow$ 1.215 $\rightarrow$ 902 ms**. Microservices chỉ scale riêng service nghẽn `Discounts` lên 3 và 6 instances giảm RT từ **2.679 $\rightarrow$ 1.233 $\rightarrow$ 1.023 ms**, không lãng phí tài nguyên cho `Products`.
- **Hạn chế:** **Không giới hạn CPU/RAM cho container Docker** khi scale; Exp 2–3 tắt API Gateway và Consul; không đo CPU/RAM và tail latency (p95/p99).

---

### 1.4. Các nghiên cứu còn lại (Nhóm Cloud Cost & Nhóm Có Biến Gây Nhiễu)
- **Villamizar et al. (2015 & 2017) — `07333476.md` & `Villamizar_et_al-2017...md`:** Trên AWS EC2/RDS với 2 dịch vụ tải khác nhau (`S1` nặng CPU 3.000 ms, `S2` nặng DB 300 ms), Microservices giảm chi phí **17%** (2015) và giảm Cost per Million Requests **9,50%–13,81%** (2017) nhờ chọn cỡ EC2 sát nhu cầu từng service; AWS Lambda giảm CMR **50,43%–77,08%**. Tuy nhiên Microservices chịu Avg RT cao hơn Monolith do bước nhảy qua API Gateway.
- **Tapia et al. (2020) — `applsci-10-05797-v2.md`:** Node.js + MySQL/MongoDB; kết quả MS (3,1 rps, 936 ms) thắng Monolith (2,5 rps, 1.150 ms) nhưng bị **biến gây nhiễu triển khai** (chạy Monolith trên máy ảo KVM và MS trên Docker), tải rất thấp (3–5 threads).
- **Wahyudin et al. (2025) — `Migrating_Monolithic_to_Microservices_Comparative.md`:** VPS 2 Core/8 GB; MS (154 ms, 16,4 rps) thắng Monolith (1.138 ms, 1 rps) nhưng bị **biến gây nhiễu công nghệ** (so sánh PHP Laravel với Golang gRPC).
- **Desina (2023) — `2305.15438v1.md`:** Không có thực nghiệm đối chứng và không có baseline Monolith; bảng số liệu minh họa có sai sót tính toán nội tại.

---

## 2. Kết luận kiến thức tổng hợp cho Nhóm 2

### 2.1. Quy luật thắng – thua giữa hai kiến trúc theo điều kiện đo
1. **Monolith / Modular Monolith thắng áp đảo** trên một máy đơn lẻ, trong giới hạn tài nguyên (resource-parity), khi giao tiếp nội bộ đồng bộ hoặc dùng in-memory queue (giảm P90 21%–24%, giảm RAM tới 3,35x, tăng throughput ~3x so với qua message broker ngoài), và khi so sánh ở cùng mức chi phí hạ tầng cloud.
2. **Microservices thắng về hiệu quả tài nguyên/chi phí** trên môi trường đa máy chủ khi tải giữa các module **không đồng đều** (CPU-bound vs. DB-bound), cho phép **selective scaling** đúng dịch vụ nghẽn cổ chai mà không phải nhân bản toàn bộ ứng dụng.

### 2.2. Bài học thiết kế thực nghiệm rút ra từ các sai lệch (Biases)
Các mâu thuẫn kết quả giữa 8 bài báo chứng minh 3 điều kiện bắt buộc phải khóa chặt trong **Chương 4** của đề tài:
- **Tech-stack & Protocol Parity:** Tuyệt đối không so PHP với Go/gRPC như Wahyudin (2025).
- **Deployment Parity:** Tuyệt đối không đặt Monolith trên KVM và MS trên Docker như Tapia (2020).
- **Resource Parity vs. Scaling Mode:** Phải tách rõ chế độ `E1 – Resource Parity` (cùng tổng trần CPU/RAM Docker như Tofan 2026) và `E2 – Scaling Evaluation` (như Krzysztoń 2024+).

### 2.3. Khoảng trống nghiên cứu trực tiếp cho đề tài
Chưa có nghiên cứu nào kết hợp đầy đủ các yếu tố sau trong cùng một thực nghiệm kiểm soát:
1. So sánh trực tiếp **Modular Monolith** (không phải Monolith cổ điển) với **Microservices** trên cùng tech stack và cùng Docker environment.
2. Áp dụng **giới hạn tài nguyên công bằng (resource-parity)** ở chế độ `E1` đồng thời đo cả **tail latency (p90/p95/p99)**, **RAM/CPU overhead**, và **độ phức tạp vận hành**.
3. Khảo sát luồng nghiệp vụ có **giao dịch đa thành phần và lỗi/bù trừ** (như xử lý đơn hàng) thay vì chỉ CRUD đơn giản hoặc endpoint không có DB.
