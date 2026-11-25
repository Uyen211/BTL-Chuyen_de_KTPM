# Literature Review — Nhóm 3: Độ phức tạp Vận hành & Thách thức Thực tế của Microservices

Nhóm tài liệu này tổng hợp các nghiên cứu thực nghiệm (khảo sát chuyên gia, phỏng vấn, khai phá GitHub issues, *Systematic Grey Literature Review* và *Systematic Literature Review*) nhằm làm rõ các đánh đổi về **độ phức tạp vận hành** khi triển khai hệ thống Microservices so với kiến trúc nguyên khối. Đây là cơ sở bằng chứng trực tiếp cho **Chương 2.8**, **Chương 3.4** và hệ thống chỉ số đo đạc ở **Chương 4.7**.

| Mã tài liệu | Tác giả & Năm | Phương pháp & Cỡ mẫu | Đóng góp chính cho đề tài |
| :--- | :--- | :--- | :--- |
| [2108.03384v2](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-3-operations-challenges-empirical/md/2108.03384v2.md) | Waseem et al. (2021) | Mixed-methods: Survey ($N=106$) + Interviews ($N=6$) | Định lượng tỷ lệ practitioner gặp khó khăn về monitoring, distributed tracing và testing trên container |
| [2302.01894v5](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-3-operations-challenges-empirical/md/2302.01894v5.md) | Waseem et al. (2023/2025) | GitHub mining (**2.641** issues từ 15 dự án) + Interviews ($N=15$) + Survey ($N=150$) | Phân loại 2.698 issue instances, 2.267 nguyên nhân và 1.936 giải pháp (CI/CD, cấu hình, giao tiếp, bảo mật) |
| [microservices-pains-gains](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-3-operations-challenges-empirical/md/microservices-pains-gains.md) | Soldani et al. (2018) | Systematic Grey Literature Review (**51** industrial studies) | Đối chiếu *Pains vs. Gains* qua 3 giai đoạn Design–Development–Operation |
| [Challenges_and_Solution_Directions_of_Microservice](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-3-operations-challenges-empirical/md/Challenges_and_Solution_Directions_of_Microservice.md) | Söylemez et al. (2022) | Systematic Literature Review (**85** primary studies từ 3.842 bài) | Taxonomy 9 nhóm thách thức (P1–P9), 40 tiểu mục và hướng giải pháp học thuật |

---

## 1. Tóm tắt chi tiết từng bài báo

### 1.1. Design, Monitoring, and Testing of Microservices Systems: The Practitioners’ Perspective — Waseem et al. (2021)
- **Nguồn:** `2108.03384v2.md` — Muhammad Waseem, Peng Liang, Mojtaba Shahin, Amleto Di Salle, Gastón Márquez.
- **Phương pháp & Cỡ mẫu:** Khảo sát trực tuyến thu được **$N=106$** phản hồi hợp lệ (từ ~9.000 email gửi đi, tỷ lệ 1,5%, đến từ 29 quốc gia) kết hợp phỏng vấn bán cấu trúc **$N=6$** chuyên gia (kinh nghiệm IT TB 11,7 năm, MSA TB 3,5 năm).
- **Phát hiện chính về độ phức tạp vận hành:**
  - **Nhân sự & Tổ chức:** **74,5%** (79/106) chưa từng được đào tạo chuyên nghiệp về MSA; **36,7%** (39/106) tổ chức không có kiến trúc sư/nhóm kiến trúc chuyên trách.
  - **Tác động dây chuyền từ thiết kế:** Thách thức thiết kế số 1 là *xác định ranh giới microservice rõ ràng* (**69,8%**, 74/106); **59,4%** cho biết điều này ảnh hưởng trực tiếp tới Monitoring và **54,7%** ảnh hưởng tới Testing.
  - **Monitoring & Tracing:** Các thách thức lớn nhất gồm thu thập metrics/logs từ container (**54,7%**, 58/106), distributed tracing (**45,3%**, 48/106), quá nhiều thành phần cần giám sát (**41,5%**, 44/106), performance monitoring (**40,6%**, 43/106), phân tích dữ liệu thu thập được (**34,9%**) và phát hiện vùng lỗi (*failure zone detection*, **34,0%**).
  - **Testing & Debugging:** Khó tạo manual tests (**50,0%**), integration testing (**43,4%**), **debug microservices trên container platforms (42,5%)**, automated tests (**38,7%**) và performance testing (**30,2%**).
- **Giải pháp ghi nhận:** DDD + Business Capability (42,3%), API Gateway (68,9%), Circuit Breaker (41,5%), ELK Stack, Prometheus + Spring Boot Actuator, Grafana, Zipkin/Jaeger, Consumer-driven contract testing.
- **Hạn chế:** Tỷ lệ phản hồi thấp (1,5%), lệch địa lý (56,6% từ Pakistan và China), 59,4% người trả lời mới có 0–2 năm kinh nghiệm MSA.

---

### 1.2. Understanding the Issues, Their Causes and Solutions in Microservices Systems: An Empirical Study — Waseem et al. (2023/2025)
- **Nguồn:** `2302.01894v5.md` — Muhammad Waseem et al.
- **Phương pháp & Cỡ mẫu:** Nghiên cứu hỗn hợp 3 pha: (1) Khai phá **2.641 closed issues** từ **15 dự án open-source** tiêu biểu (Spinnaker, Jaeger, eShopOnContainers, Spring PetClinic, v.v.); (2) Phỏng vấn **$N=15$** chuyên gia; (3) Khảo sát xác thực **$N=150$** chuyên gia từ 42 quốc gia. Tổng hợp **2.698 issue instances**, **2.267 cause instances** và **1.936 solution instances**.
- **Phát hiện chính:**
  - **Phân bố issues (GitHub mining):** *Technical Debt* (**25,46%**, 687 instances), *CI/CD Issue* (**11,60%**, 313 — gồm Deployment/Delivery 105, Kubernetes 74, Docker 50), *Exception Handling* (**8,45%**, 228), *Service Execution & Communication* (**8,11%**, 219), *Security* (**7,89%**, 213), *Build Issue* (**7,78%**, 210), *Configuration Issue* (**4,48%**, 121), *Monitoring Issue* (**3,29%**, 89), *Testing* (**2,85%**, 77).
  - **Xác thực qua khảo sát ($N=150$, mức *Very Often + Often*):** *Security* (**82,67%**), *Organizational Issue* (**82,67%** — vốn chỉ chiếm 0,25% trên GitHub issue tracker), *Technical Debt* (**70,67%**), *CI/CD* (**69,34%**), *Performance* (**63,33%**), *Service Execution & Communication* (**60,00%**), *Testing* (**59,34%**), *Monitoring* (**52,67%**), *Configuration* (**52,67%**).
  - **Nguyên nhân gốc (2.267 instances):** Lỗi lập trình chung (**37,93%**), thiếu tính năng/artifact (**17,02%**), **cấu hình & giao tiếp sai (16,85%**, riêng Incorrect Configuration 12,79%), và **tương thích phiên bản/dependency cũ (9,79%)**.
- **Giải pháp ghi nhận:** Hơn 84% giải pháp thực tế mang tính cục bộ (*Fix/Add/Modify Artifacts*); các giải pháp cấp hệ thống gồm Service Mesh, API Gateway, Message Broker (Kafka/RabbitMQ), CI/CD tự động hóa, Trace ID logging.
- **Hạn chế:** Dữ liệu OSS lệch về các dự án lớn; chỉ phân tích closed issues; tỷ lệ Organizational Issues trên GitHub rất thấp so với thực tế khảo sát.

---

### 1.3. The Pains and Gains of Microservices: A Systematic Grey Literature Review — Soldani et al. (2018)
- **Nguồn:** `microservices-pains-gains.md` — Jacopo Soldani, Damian Andrew Tamburri, Willem-Jan Van Den Heuvel.
- **Phương pháp & Cỡ mẫu:** *Systematic Grey Literature Review (GLR)* tuyển chọn **51 industrial studies** (2014–2017) từ các doanh nghiệp vận hành thực tế (Netflix, Amazon, Microsoft, ThoughtWorks, Pivotal, v.v.), kiểm soát độ tin cậy mã hóa với Krippendorff’s $\alpha$ đạt **0,92**.
- **Phát hiện chính (*Pains vs. Gains* trong 51 studies):**
  - **Gains:** Scalability (**31/51**), Loose coupling (**27/51**), Bounded contexts (**24/51**), Technology freedom (**24/51**), Independent deployment (**19/51**), CI/CD (**15/51**), Fault isolation (**14/51**).
  - **Pains theo vòng đời:**
    - *Design:* Size/complexity (**27/51**), Service dimensioning (**16/51**), API versioning (**13/51**), Endpoint proliferation (**7/51**).
    - *Development:* **Data consistency (21/51)**, **Distributed transactions (18/51)**, **Performance testing (16/51)**, Query complexity (**9/51**).
    - *Operation:* **Operational complexity (26/51)**, Monitoring complexity (**21/51**), **Network consumption cao (17/51)**, **Distributed logging (12/51)**, **Problem location / tìm nguyên nhân gốc (9/51)**, Cascading failures (**7/51**), Compute consumption cao (**7/51**).
- **Hạn chế:** Grey literature chỉ đếm tần suất xuất hiện, **chưa đo được mức độ nghiêm trọng định lượng** (*"how much each pain is actually paining"*); dữ liệu dừng ở cuối 2017 trước khi Kubernetes/Service Mesh phổ biến rộng.

---

### 1.4. Challenges and Solution Directions of Microservice Architectures: A Systematic Literature Review — Söylemez et al. (2022)
- **Nguồn:** `Challenges_and_Solution_Directions_of_Microservice.md` — Mehmet Söylemez, Bedir Tekinerdogan, Ayça Kolukısa Tarhan (*Applied Sciences*, 2022).
- **Phương pháp & Cỡ mẫu:** SLR trên 5 CSDL (ACM, IEEE, ScienceDirect, Springer, Wiley) giai đoạn 01/2014–02/2022; lọc từ **3.842 bài** còn **85 primary studies** (`57,64%` single-case study, `25,88%` multiple-case study, `16,48%` descriptive).
- **Taxonomy 9 nhóm thách thức vận hành (P1–P9, 40 tiểu mục):**
  - *P1. Service Discovery* (độ trễ runtime, HA cho registry).
  - *P2. Data Management & Consistency* (distributed transactions, đánh đổi BAC).
  - *P3. Testing* (resilience, performance, regression testing trong CI/CD).
  - *P4. Performance Prediction & Optimization* (tải động).
  - *P5. Communication & Integration* (cascading failures, áp lực mạng container).
  - *P6. Service Orchestration* (nhiều nghiên cứu nhất: cấp phát tài nguyên động, stateful storage, auto-scaling threshold, hành vi failure–recovery của container).
  - *P7. Security* (endpoint attack surface, access control phân tán).
  - *P8. Monitoring, Tracing & Logging* (log dị thể, root-cause localization).
  - *P9. Decomposition* (granularity ảnh hưởng trực tiếp tới scalability và performance).
- **Hạn chế:** Thiên lệch xuất bản học thuật (publication bias); không benchmark đối chiếu định lượng giữa các giải pháp; 30,6% (26/85) bài sơ cấp có điểm chất lượng $<6/8$.

---

## 2. Kết luận kiến thức tổng hợp cho Nhóm 3

### 2.1. Đồng thuận thực nghiệm về 5 "nỗi đau vận hành" lớn nhất của Microservices
Qua cả 4 nghiên cứu (tổng hợp hàng nghìn issues, >250 chuyên gia khảo sát/phỏng vấn, 51 tài liệu công nghiệp và 85 bài báo học thuật), giới nghiên cứu và thực hành thống nhất 5 nguồn phát sinh độ phức tạp vận hành mà Monolith / Modular Monolith tránh được hoặc giảm thiểu mạnh:
1. **Giám sát, Truy vết & Định vị lỗi (Observability & Root-Cause Localization):** Thu thập logs/metrics từ nhiều container (54,7%), distributed tracing (45,3%), log dị thể và xác định vùng lỗi (34,0%).
2. **CI/CD, Build & Trôi dạt Cấu hình (Configuration & Dependency Drift):** Bùng nổ lỗi pipeline CI/CD (11,6% issues; 69,3% gặp thường xuyên), sai cấu hình (12,8% nguyên nhân) và xung đột phiên bản giữa các dịch vụ.
3. **Giao tiếp mạng & Lỗi dây chuyền:** Tăng tiêu thụ mạng (17/51), lỗi kết nối/discovery (8,1% issues) và nguy cơ cascading failures (7/51).
4. **Kiểm thử & Debug phân tán:** Khó viết test tích hợp (43,4%), test hiệu năng (30,2%–31,4%) và debug bên trong container (42,5%).
5. **Nhất quán dữ liệu, Bảo mật & Chi phí Tổ chức:** Giao dịch phân tán/nhất quán dữ liệu (21/51), bề mặt tấn công nhiều endpoint (7,9% issues; 82,7% lo ngại) và gánh nặng nhân sự/công cụ (82,7% gặp vấn đề tổ chức).

### 2.2. Hệ thống chỉ số đo Độ phức tạp Vận hành đề xuất cho Chương 4.7
Để khắc phục khoảng trống do Soldani et al. (2018) chỉ ra (chưa định lượng hóa mức độ "đau" vận hành) và tuân thủ nguyên tắc **giữ từng chỉ số độc lập** của [huongdan.md](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/guide/huongdan.md), Chương 4.7 nên đo 5 nhóm chỉ số khách quan sau khi triển khai hai hệ thống mẫu:
1. **Deployment Footprint & Config Surface:** Số lượng container/service units, số lượng file cấu hình (Dockerfile, Compose/K8s manifests) và số biến môi trường.
2. **Build & Deployment Effort:** Thời gian build toàn hệ thống, thời gian dựng môi trường từ đầu (*environment setup time*) và thời gian deploy.
3. **Observability & Fault Diagnosis:** Độ sâu chuỗi gọi (*call-chain depth*), số nguồn log cần tổng hợp, và thời gian khoanh vùng dịch vụ lỗi khi tiêm sự cố (*Fault Injection / MTTD*).
4. **Verification Surface:** Số lượng API contracts / integration points cần kiểm thử liên dịch vụ.
5. **Runtime Blast Radius:** Tỷ lệ lỗi lan truyền khi một thành phần (ví dụ `Payment` hoặc `Inventory`) bị trễ hoặc sập trong kịch bản Fault Injection.
