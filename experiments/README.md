# Thư mục Mã nguồn Thực nghiệm (`experiments/`)

Thư mục này chứa mã nguồn và cấu hình hạ tầng cho **Chương 4 & Chương 5**, triển khai theo thiết kế tại [chuong_4_thiet_ke_thuc_nghiem.md](../docs/chuong_4_thiet_ke_thuc_nghiem.md).

## Cấu trúc dự kiến

- `modular-monolith/` — Phiên bản Java 21 + Spring Boot 3 + Spring Modulith (4 mô-đun: `order`, `inventory`, `payment`, `notification`; 1 PostgreSQL với 4 schemas).
- `microservices/` — Phiên bản Java 21 + Spring Boot 3 + Spring Cloud Gateway + RabbitMQ + 4 PostgreSQL instances (*Database per Service*).
- `k6/` — Kịch bản kiểm thử tải `K1`–`K5` (`Load`, `Stress`, `Spike`, `Fault Injection`, `Selective Scaling`).
- `monitoring/` — Cấu hình `Prometheus`, `cAdvisor` và `Grafana` dashboards.
- `results/` — Kết quả đo thô, log thời gian build/deploy/MTTD và script kiểm định thống kê (Mann-Whitney U, Cliff's Delta).
