# Research Matrix — Khung Kiểm soát Chất lượng Học thuật (Chương 1–6)

Tài liệu này liên kết từng mục trong cấu trúc 6 chương của [huongdan.md](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/guide/huongdan.md) với **câu hỏi cần trả lời**, **nguồn tài liệu từ 4 nhóm đã tổng hợp**, **bằng chứng cụ thể**, và **loại lập luận được phép sử dụng** (`T1` Lý thuyết, `E1` Thực nghiệm từ paper có điều kiện đo, `C1` Case study, `S1` Khảo sát/Mining, `A1` Phân tích suy luận có đánh dấu rõ, `EXP` Dữ liệu tự đo ở Chương 5).

---

## Phần I: Khung viết Giai đoạn 2 & 3 (Nghiên cứu Lý thuyết & Phân tích So sánh)

### Chương 1. Giới thiệu đề tài *(Viết hoàn chỉnh sau khi chốt Research Gap ở Chương 3)*

| Mục | Câu hỏi / Yêu cầu cốt lõi | Nguồn tài liệu chính | Bằng chứng trích xuất | Loại lập luận |
| :--- | :--- | :--- | :--- | :---: |
| **1.1** Bối cảnh nghiên cứu | Tại sao doanh nghiệp quan tâm trở lại Modular Monolith thay vì mặc định chọn Microservices? | `2401.11867v1`, `microservices-pains-gains` | Xu hướng tăng tài liệu 2019–2023; 4 case Shopify, Appsmith, Gusto, PlayTech; sự đánh đổi Gains vs. Pains (26/51 operational complexity) | `C1` + `A1` |
| **1.2** Vấn đề nghiên cứu | Hai kiến trúc cùng nghiệp vụ nhưng khác cấu trúc triển khai ảnh hưởng thế nào đến hiệu năng và chi phí vận hành? | `2201.07226v1`, `Tail_latency...`, `Comparative_analysis...` | Sự tồn tại của overhead ngay từ DTO/module boundary (Faustino) đến network/RAM overhead (Tofan, Krzysztoń) | `E1` + `A1` |
| **1.3–1.4** Mục tiêu & `RQ1`–`RQ5` | Chuẩn hóa 5 câu hỏi: hiệu năng (`RQ1`), tài nguyên (`RQ2`), dữ liệu (`RQ3`), vận hành (`RQ4`), điều kiện lợi thế (`RQ5`) | Toàn bộ khung `huongdan.md` + Gap ở Chương 3.7 | Ánh xạ 1–1 từ `RQ1`–`RQ5` sang các mục của Chương 3 và Chương 4–5 | `A1` |
| **1.5–1.7** Phạm vi, Phương pháp & Đóng góp | Xác định rõ giới hạn (single-node Docker resource-parity vs. scaling), phương pháp *Comparative + Controlled Experiment* | `huongdan.md`, Nhóm 2 & 3 | Làm rõ phạm vi đối chiếu công bằng để tránh khái quát hóa quá mức | `A1` |

---

### Chương 2. Cơ sở lý thuyết *(Mỗi mục phải trả lời: Nguyên lý này tác động thế nào đến hai kiến trúc?)*

| Mục | Câu hỏi / Yêu cầu cốt lõi | Nguồn tài liệu chính | Bằng chứng trích xuất | Loại lập luận |
| :--- | :--- | :--- | :--- | :---: |
| **2.1** Tổng quan kiến trúc phần mềm | Quality Attributes (Performance, Scalability, Modifiability, Deployability) liên quan thế nào? | `huongdan.md`, `Challenges_and_Solution...` | Định nghĩa chuẩn thuộc tính chất lượng làm trục đánh giá xuyên suốt | `T1` |
| **2.2** Nguyên lý thiết kế module | Modularity & Information Hiding khác gì với phân tách process vật lý? | `On_the_Criteria...` (Parnas 1972/2001) | Module = *work assignment*; secrets sau abstract interface; quan hệ `"uses"`; cảnh báo gắn module với process gây overhead | `T1` |
| **2.3** Kiến trúc Modular Monolith | Thế nào là Modular Monolith đúng nghĩa (khác Monolith truyền thống)? | `2401.11867v1` (Su & Li 2024), `2201.07226v1` | 6 đặc trưng (tầng trong module, loose coupling, unified DB schema, single deployment unit), 9 tính chất, Spring Modulith / Service Weaver | `T1` + `C1` |
| **2.4** Kiến trúc Microservices | Các thành phần bắt buộc của Microservices là gì? | `modernization-data-persistence`, `microservices-pains-gains` | Service independence, Database per service, API Gateway, Service Discovery, Message Broker, Containerization | `T1` + `C1` |
| **2.5** Nguyên lý hệ thống phân tán | Chi phí nào phát sinh khi chuyển từ in-process call sang network call? | `TheTailAtScale`, `dapper-2010-1`, `2201.07226v1` | Serialization/deserialization (chiếm 82% latency ở Faustino), khuếch đại tail latency (fan-out 100 servers $\rightarrow$ 63% > 1s), tracing overhead (+16,3% nếu trace 100%) | `T1` + `E1` |
| **2.6** Quản lý giao dịch & dữ liệu | Tại sao không thể giữ ACID xuyên dịch vụ và cái giá của Saga/Outbox là gì? | `GL-cap`, `38713.38742`, `modernization-data-persistence` | CAP Theorem (Theorem 1, 2); LLT deadlock $\propto \text{size}^4$; Saga + $C_i$ nới lỏng isolation; 6 patterns AWS (API Composition giảm availability) | `T1` |
| **2.7** Nguyên lý & chỉ số hiệu năng | Vì sao phải đo p50/p95/p99 thay vì chỉ đo trung bình? | `TheTailAtScale`, `Tail_latency...` | Khái niệm tail latency, throughput, CPU/RAM utilization, Open vs. Closed load model | `T1` |
| **2.8** Nguyên lý vận hành hệ thống | Những gánh nặng CI/CD, Observability và chẩn đoán lỗi nào xuất hiện? | `2108.03384v2`, `2302.01894v5`, `dapper-2010-1`, `Challenges_and_Solution...` | Thu thập log/metrics container (54,7%), distributed tracing (45,3%), debug container (42,5%), CI/CD & config drift (11,6% & 16,85%) | `T1` + `S1` |

---

### Chương 3. Tổng quan nghiên cứu và Phân tích so sánh *(Cầu nối lý thuyết $\rightarrow$ thực nghiệm)*

| Mục | Câu hỏi / Yêu cầu cốt lõi | Nguồn tài liệu chính | Bằng chứng trích xuất | Loại lập luận |
| :--- | :--- | :--- | :--- | :---: |
| **3.1** Tổng quan nghiên cứu liên quan | Các nhánh nghiên cứu đã đi đến đâu (hiệu năng, mở rộng, vận hành, Modular Monolith)? | Toàn bộ Nhóm 1, 2, 3 | Hệ thống hóa theo 4 nhánh: Modular Monolith, Benchmark hiệu năng, Cloud cost, Khảo sát vận hành | `E1` + `S1` + `C1` |
| **3.2** So sánh thiết kế & cấu trúc | Ranh giới module vs. ranh giới dịch vụ; chi phí tái cấu trúc & mở rộng đội ngũ | `On_the_Criteria...`, `2401.11867v1`, `2201.07226v1`, `2108.03384v2` | Sửa 40%–82% entities khi modular hóa; 69,8% gặp khó xác định ranh giới MS; chi phí sửa sai service boundary (Gusto) | `T1` + `E1` + `S1` |
| **3.3** So sánh tính toàn vẹn & nhất quán dữ liệu | ACID nội bộ vs. Database-per-service, Saga, Eventual Consistency | `38713.38742`, `modernization-data-persistence`, `microservices-pains-gains`, `2201.07226v1` | 21/51 gặp khó data consistency, 18/51 distributed tx; rủi ro lan truyền khi có sự cố/xóa dữ liệu (LdoD Table V) | `T1` + `C1` + `E1` |
| **3.4** So sánh độ phức tạp vận hành | CI/CD, monitoring, tracing, fault diagnosis & configuration drift khác nhau ra sao? | `2108.03384v2`, `2302.01894v5`, `microservices-pains-gains`, `Challenges_and_Solution...` | 26/51 operational complexity; 82,67% gặp vấn đề security & organizational; 16,85% lỗi từ cấu hình/giao tiếp sai | `S1` + `C1` |
| **3.5** So sánh hiệu năng & tài nguyên | Khi nào Monolith/Modular thắng, khi nào MS thắng? Vai trò của serialization, broker & scaling? | `Monolithic_vs_Microservice...`, `Tail_latency...`, `Comparative_analysis...`, `Villamizar 2015/2017` | Single-node/resource-parity: Mono P90 thấp hơn 21–24%, RAM thấp 3,35x (Tofan); in-memory queue nhanh 3x RabbitMQ (Krzysztoń); Cloud selective scaling giảm 9,5%–17% chi phí (Villamizar) | `E1` + `A1` |
| **3.6** Bảng tổng hợp nghiên cứu trước | Đối chiếu trung thực các công trình (Phương pháp, Chỉ số, Kết quả, Điều kiện, Hạn chế) | Bảng tại `docs/evidence_table.md` | Chỉ trích xuất từ các paper có thực nghiệm/khảo sát thật (loại bỏ `Desina 2023` khỏi bảng định lượng vì thiếu baseline) | `E1` + `S1` |
| **3.7** Khoảng trống nghiên cứu (Research Gap) | Điểm nào các nghiên cứu trước chưa giải quyết triệt để? | Giao điểm hạn chế của `Tofan (2026)`, `Krzysztoń (≥2024)`, `Faustino (2022)`, `Soldani (2018)` | (1) Thiếu đối chiếu **Modular Monolith vs. MS** trong **Docker resource-parity**; (2) Thiếu đo đồng thời **tail latency + RAM/CPU + chỉ số vận hành định lượng**; (3) Nhiều bài bị nhiễu stack/platform (`Wahyudin`, `Tapia`) | `A1` |
| **3.8** Giả thuyết nghiên cứu ($H_1 \dots H_5$) | Phát biểu các dự đoán có thể kiểm định bằng thực nghiệm | Rút từ 3.2–3.7 & `huongdan.md` | $H_1$ (độ trễ), $H_2$ (tài nguyên nền), $H_3$ (độ phức tạp triển khai), $H_4$ (selective scaling), $H_5$ (chi phí nhất quán dữ liệu) | `A1` *(chưa chứng minh)* |

---

## Phần II: Khung thiết kế Giai đoạn 4 & Dự phòng Chương 5–6

### Chương 4. Thiết kế và Triển khai thực nghiệm *(Chốt trước khi lập trình & chạy k6)*

| Mục | Nội dung cần chốt | Tham chiếu kế thừa từ Literature | Nguyên tắc kiểm soát (Fairness) |
| :--- | :--- | :--- | :--- |
| **4.1–4.2** Mục tiêu & Nghiệp vụ mẫu | Luồng xử lý đơn hàng: `Order`, `Inventory`, `Payment`, `Notification` (gồm luồng thành công và luồng lỗi cần hoàn tác/bù trừ) | `Tail_latency...` (`POST /orders`), `38713.38742` (Saga) | Hợp đồng API đầu vào/đầu ra giống hệt nhau giữa 2 kiến trúc |
| **4.3–4.4** Kiến trúc & Công nghệ | Hai phiên bản: **Modular Monolith** (module boundary rõ ràng, 1 process, 1 DB với schema/table cô lập) vs. **Microservices** (tách service + DB riêng, qua Gateway/HTTP hoặc broker) | `2401.11867v1` (Spring Modulith / modular boundary), `Comparative_analysis...` | **Tech-stack parity** (cùng ngôn ngữ, framework, DB engine) và **Deployment parity** (cùng Docker Compose) |
| **4.5–4.6** Kịch bản tải & Chỉ số hiệu năng | Chế độ **`E1 – Resource Parity`** (cùng tổng trần CPU/RAM Docker như Tofan 2026) và tùy chọn **`E2 – Scaling Evaluation`**; đo bằng **k6** + **Prometheus/Grafana** (Load thấp/TB/cao, Stress, Spike, Fault Injection) | `huongdan.md` Mục 5.1, `Tail_latency...`, `TheTailAtScale` | Đo p50/p95/p99, Throughput (RPS), Error Rate, CPU%, RAM (MiB) và Resource per Request |
| **4.7** Đo độ phức tạp vận hành | Giữ **5 nhóm chỉ số độc lập** (không cộng thành 1 điểm tùy ý): số container/config, build/deploy/setup time, call-chain depth & MTTD khi Fault Injection, số integration contracts, blast radius | `huongdan.md` Mục 5.2 + Tổng hợp Nhóm 3 | Định lượng hóa "operational pains" mà Soldani (2018) nêu là còn thiếu |
| **4.8–4.9** Thống kê & Threats to Validity | Lặp nhiều lần, dùng kiểm định phi tham số (như Mann-Whitney U) nếu phân phối lệch; ghi nhận trước giới hạn 1 máy chủ / local Docker | `Tail_latency...`, `Blinowski 2022` | Không suy diễn kết quả single-node sang kết luận về multi-node cloud |

### Chương 5 & Chương 6 *(Chỉ viết sau khi có dữ liệu thực nghiệm thật)*
- **Chương 5 (Kết quả & Thảo luận):** Đối chiếu trực tiếp dữ liệu đo thực tế (`EXP`) với giả thuyết $H_1 \dots H_5$ và kết quả của `Faustino (2022)`, `Tofan (2026)`, `Krzysztoń (≥2024)`, `Blinowski (2022)`, `Waseem (2021/2025)` — giải thích điểm tương đồng và khác biệt dựa trên điều kiện đo.
- **Chương 6 (Kết luận):** Trả lời dứt khoát `RQ1`–`RQ5` trong đúng phạm vi đã kiểm chứng.

---

## Phần III: Checklist Kiểm soát Chống Hallucination khi Viết

- [ ] Mọi con số trích từ paper đều ghi kèm **tác giả + năm + môi trường/công cụ đo**.
- [ ] Không vẽ biểu đồ radar, heatmap tự chấm điểm 1–5, hay biểu đồ số liệu mô phỏng ở Chương 1–4.
- [ ] Các biểu đồ ở Chương 2–3 chỉ là **sơ đồ nguyên lý kiến trúc / luồng xử lý** hoặc số liệu trích nguyên văn từ paper có ghi nguồn.
- [ ] Phần văn xuôi tiếng Việt tuân thủ chuẩn mực học thuật trong [write-skill.md](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/guide/write-skill.md) (tránh câu cụt, tránh liệt kê máy móc, lập luận mạch lạc).
