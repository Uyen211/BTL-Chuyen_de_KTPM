# Literature Review — Nhóm 1: Modular Monolith và Lộ trình Chuyển đổi (Migration)

Nhóm tài liệu này tập trung vào bản chất kiến trúc **Modular Monolith**, hệ sinh thái công cụ hỗ trợ, các trường hợp áp dụng thực tế trong công nghiệp, và bằng chứng định lượng về chi phí tái cấu trúc (migration effort) cũng như hiệu năng khi chuyển đổi từng bước từ Monolith $\rightarrow$ Modular Monolith $\rightarrow$ Microservices.

| Mã tài liệu | Tác giả & Năm | Phương pháp nghiên cứu | Đóng góp chính cho đề tài |
| :--- | :--- | :--- | :--- |
| [2401.11867v1](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-1-modular-monolith-migration/md/2401.11867v1.md) | Su & Li (2024) | Systematic Grey Literature Review (64 tài liệu) | Chuẩn hóa định nghĩa, 6 đặc trưng, 9 tính chất, 3 framework và 4 case công nghiệp chọn Modular Monolith |
| [2201.07226v1](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-1-modular-monolith-migration/md/2201.07226v1.md) | Faustino et al. (2022) | Case study thực nghiệm (*LdoD Archive*, Java/Spring Boot) | Đo trực tiếp migration effort và hiệu năng (latency, throughput) qua cả 3 mốc: Monolith, Modular Monolith, Microservices |

---

## 1. Tóm tắt chi tiết từng bài báo

### 1.1. Modular Monolith: Is This the Trend in Software Architecture? — Su & Li (2024)
- **Nguồn:** `2401.11867v1.md` — Ruoyu Su, Xiaozhou Li (M3S, University of Oulu, Finland).
- **Mục tiêu & Phương pháp:** Thực hiện *Systematic Grey Literature Review (SGLR)* theo hướng dẫn của Garousi et al. và Keele et al., kết hợp *snowballing*. Truy vấn Google với từ khóa liên quan `"modular monolith"`, `"service weaver"`, `"microservice(s)"` thu được **140 kết quả**, lọc còn **64 tài liệu** (`[S1]`–`[S64]`, giai đoạn 2019–2023, tăng mạnh năm 2023) để trả lời 3 câu hỏi nghiên cứu: `RQ1` (47/64 tài liệu — Định nghĩa), `RQ2` (17/64 tài liệu — Frameworks), `RQ3` (6/64 tài liệu — Cases thực tế).
- **Kết quả chính:**
  - **6 đặc trưng cốt lõi của Modular Monolith:** (1) Phân tách module theo các tầng riêng (`Domain`, `Infrastructure`, `API`); (2) Loose coupling & high cohesion (giao tiếp qua API nội bộ, ưu tiên bất đồng bộ); (3) Unified Database Schema (chung một schema); (4) Monolithic Deployment Structure (triển khai như một đơn vị duy nhất trên cùng VM hoặc dedicated VMs); (5) Unified Application Process (một tiến trình duy nhất, không tách cứng data ownership); (6) Cải thiện khả năng bảo trì và mở rộng so với monolith truyền thống.
  - **9 tính chất nổi bật:** Phụ thuộc tối thiểu giữa các module; khả năng thay thế/tái sử dụng code; quản lý dependency tốt hơn monolith truyền thống; triển khai một single unit không cần nhiều server; ít phức tạp hơn microservices; giao tiếp qua public interface/API được định nghĩa rõ.
  - **3 Frameworks đại diện:** *Service Weaver* (Google, Go, bản `v0.1` — tách logic khỏi triển khai, tự động chọn method call cục bộ hoặc RPC từ xa), *Spring Modulith* (Spring Boot — tổ chức module theo sub-packages, kiểm soát Bean exposure, transaction event log, runtime observability cấp module), *Light-hybrid-4j* (nạp nhiều `.jar` service vào cùng JVM trong Docker volume).
  - **4 Industry Cases chọn Modular Monolith thay cho Microservices:** *Shopify* (Ruby on Rails, >1.000 developers — cân bằng single codebase với clear component boundaries), *Appsmith* (từ bỏ microservices do độ phức tạp triển khai on-premise), *Gusto* (tránh chi phí sửa sai service boundary và độ phức tạp test/deploy), *PlayTech* (tránh maintenance overhead không cần thiết ở quy mô một team).
- **Hạn chế:** Không có mục *Threats to validity* riêng; không thực hiện benchmark hiệu năng; *Service Weaver* mới ở giai đoạn đầu (`v0.1`).
- **Ý nghĩa với đề tài:** Là nền tảng học thuật trực tiếp giúp phân biệt **Modular Monolith** với **Monolith truyền thống** (Chương 2.3), đồng thời cung cấp bằng chứng định tính từ doanh nghiệp về **độ phức tạp vận hành** của Microservices (Chương 3.4).

---

### 1.2. Stepwise Migration of a Monolith to a Microservices Architecture: Performance and Migration Effort Evaluation — Faustino et al. (2022)
- **Nguồn:** `2201.07226v1.md` — Diogo Faustino, Nuno Gonçalves, Manuel Portela, António Rito Silva.
- **Mục tiêu & Phương pháp:** Đánh giá lộ trình chuyển đổi từng bước (*stepwise migration*) từ Monolith có *rich domain model* sang Microservices thông qua bước đệm **Modular Monolith**, đo cả **migration effort**, **hiệu năng** (latency, throughput) và phân tích **data consistency**.
- **Thiết lập thực nghiệm & Điều kiện đo:**
  - **Hệ thống:** *LdoD Archive* (Java, Spring Boot, ORM; **25.862** dòng Java, **20.039** dòng JSP, **7.721** dòng JS; **71 domain entities**, **81 bidirectional relations**), tách thành 5 modules/services (`Text`: 42 entities, `User`: 5, `Virtual`: 17, `Recommendation`: 2, `Game`: 5). Phiên bản Microservices dùng synchronous REST API cho `uses` và asynchronous message broker cho `notification`.
  - **Phần cứng & Công cụ:** Docker containers trên máy chuyên dụng **Intel i7 (6 cores), 16GB RAM, 1TB SSD**. Công cụ **JMeter** gửi **50 requests tuần tự** (sau 1 request warm-up cache) trên 4 tác vụ (*Source Listing*, *Fragment Listing*, *Interpretation View*, *Assisted Ordering*) ở 2 mức dữ liệu (**100 fragments** và **720 fragments**).
- **Kết quả định lượng chính:**
  - **Migration Effort (Monolith $\rightarrow$ Modular Monolith):** Phải chỉnh sửa **40%–82% entities** tùy module (ví dụ: `Virtual` sửa `14/17` = 82%, `Text` sửa `23/42` = 55%) và định nghĩa mới DTOs (như `Virtual` `7/17` = 41%). Khi chuyển tiếp sang **Microservices**, phải sửa **83%–100%** các phương thức trên provides/requires interfaces để map sang HTTP endpoints và xử lý dữ liệu không serializable.
  - **Hiệu năng (định dạng `100 fragments / 720 fragments`):**
    - *Source Listing:* Latency (ms) từ Monolith `17 / 61` $\rightarrow$ Modular `22 / 629` (`+29% / +931%`) $\rightarrow$ Microservices `438 / 4317` (`+2476% / +6977%` so với Monolith). Throughput (req/s) giảm từ `55.1 / 16.2` $\rightarrow$ `43.7 / 1.6` $\rightarrow$ `2.3 / 0.23`. Ngay cả khi đã tối ưu coarse-grained DTO, **serialization/deserialization chiếm 82%** độ trễ trung bình (>3.000 ms serialization, 560 ms deserialization).
    - *Fragment Listing:* Latency (ms) `103 / 350` (Monolith) $\rightarrow$ `61 / 1095` (Modular) $\rightarrow$ `725 / 5715` (Microservices). Ở mức 100 fragments, Modular nhanh hơn Monolith (`-41%`) nhờ đánh DB index cho unique IDs.
    - *Interpretation View:* Latency (ms) `29 / 25` (Monolith) $\rightarrow$ `24 / 37` (Modular) $\rightarrow$ `155 / 140` (Microservices).
    - *Assisted Ordering:* Latency (ms) `137 / 3801` (Monolith) $\rightarrow$ `165 / 12295` (Modular) $\rightarrow$ `886 / 11444` (Microservices — có thêm 2 caches ở `Recommendation` service).
  - **Data Consistency:** Trong 8 loại event phân tích, các event xóa ở `Text` và `User` có tác động lan truyền cao nhưng tần suất thấp (`Low`), nên *eventual consistency* đáp ứng được mà chưa cần Saga phức tạp.
- **Hạn chế:** Chỉ đánh giá trên một case study đơn lẻ (*LdoD Archive*) viết theo mô hình *rich domain model* trên Spring Boot; workload JMeter chỉ chạy **50 requests tuần tự** (chưa kiểm thử tải đồng thời cao — concurrent load).
- **Ý nghĩa với đề tài:** Là bằng chứng thực nghiệm hiếm hoi đo trực tiếp **Modular Monolith vs. Microservices** trên cùng hệ thống thật; chỉ ra rõ nguyên nhân suy giảm hiệu năng khác nhau giữa hai kiến trúc (Modular Monolith nhạy với **kích thước DTO**, còn Microservices nhạy với cả **số lần gọi mạng** và **chi phí serialization/deserialization**).

---

## 2. Kết luận kiến thức tổng hợp cho Nhóm 1

1. **Định vị đúng Modular Monolith:** Modular Monolith không phải là Monolith truyền thống chia tầng kỹ thuật, mà là kiến trúc phân rã theo miền nghiệp vụ (*Bounded Context / Domain*) với ranh giới interface rõ ràng, loose coupling và triển khai thành một đơn vị duy nhất.
2. **Chi phí ẩn xuất hiện sớm hơn kỳ vọng:** Ngay ở bước Modular Monolith, việc ép ranh giới module (loại bỏ liên kết ORM chéo, dùng unique IDs + DTOs) đã đòi hỏi sửa đổi lượng lớn domain entities và phát sinh overhead chuyển đổi DTO khi payload lớn. Tuy nhiên, mức suy giảm của Microservices vẫn cao hơn gấp nhiều lần do giao tiếp mạng và serialization.
3. **Động lực vận hành là yếu tố quyết định trong công nghiệp:** Các case study (Shopify, Appsmith, Gusto, PlayTech) cho thấy doanh nghiệp chọn Modular Monolith chủ yếu để tránh **độ phức tạp vận hành** (triển khai on-premise, quản lý nhiều repo/pipeline, kiểm thử tích hợp phân tán, chi phí sửa sai service boundary).
4. **Hệ quả cho thiết kế thực nghiệm (Chương 4):**
   - Nên cân nhắc chọn **Spring Modulith** (Java/Spring Boot) hoặc cấu trúc module boundary tường minh để đảm bảo phiên bản Modular Monolith thực sự tuân thủ ranh giới module.
   - Kịch bản kiểm thử cần bao quát cả **tác vụ nhiều dữ liệu (large DTO/payload)** lẫn **tác vụ nhiều lời gọi liên module (chatty calls)**, đồng thời khắc phục hạn chế của Faustino et al. bằng cách kiểm thử **tải đồng thời (concurrent load)** với k6 và đo **tài nguyên CPU/RAM**.
