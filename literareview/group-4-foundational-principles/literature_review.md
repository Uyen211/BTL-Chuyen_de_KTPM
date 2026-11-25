# Literature Review — Nhóm 4: Các Nguyên lý Nền tảng (Kỹ thuật Phần mềm & Hệ thống Phân tán)

Nhóm tài liệu này tập hợp **6 công trình nền tảng** giải thích bản chất tại sao việc chuyển từ lời gọi hàm trong cùng tiến trình (**Modular Monolith**) sang giao tiếp qua mạng và tách dữ liệu (**Microservices**) làm thay đổi căn bản hành vi về cấu trúc, tính nhất quán dữ liệu, độ trễ đuôi và khả năng quan sát. Đây là trục lý thuyết xương sống cho **Chương 2 (các mục 2.2, 2.5, 2.6, 2.7, 2.8)**.

| Mã tài liệu | Tác giả & Năm | Chủ đề nền tảng | Đóng góp trực tiếp cho Chương 2 |
| :--- | :--- | :--- | :--- |
| [On_the_Criteria_To_Be_Used_in_Decomposing_Systems](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-4-foundational-principles/md/On_the_Criteria_To_Be_Used_in_Decomposing_Systems.md) | Parnas (1972 / ~2001) | Information Hiding & Phân rã Module | Mục 2.2 & 2.3: Chứng minh module hóa là nguyên lý logic, độc lập với process vật lý |
| [GL-cap](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-4-foundational-principles/md/GL-cap.md) | Gilbert & Lynch (2002) | Định lý CAP (Brewer's Conjecture) | Mục 2.5 & 2.6: Giới hạn bất khả thi giữa Consistency, Availability và Partition Tolerance |
| [38713.38742](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-4-foundational-principles/md/38713.38742.md) | Garcia-Molina & Salem (1987) | Sagas & Long-Lived Transactions | Mục 2.6: Lý do tránh global ACID lock và cơ chế bù trừ ngữ nghĩa |
| [modernization-data-persistence](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-4-foundational-principles/md/modernization-data-persistence.md) | Ward & Mohan / AWS (2021–2025) | 6 Patterns lưu trữ dữ liệu Microservices | Mục 2.4 & 2.6: Đánh đổi thực tế giữa Database-per-service, Shared-DB, CQRS, Saga |
| [TheTailAtScale](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-4-foundational-principles/md/TheTailAtScale.md) | Dean & Barroso (2013) | Tail Latency & Fan-out Amplification | Mục 2.5 & 2.7: Giải thích khuếch đại độ trễ đuôi p99/p99.9 khi gọi nhiều dịch vụ |
| [dapper-2010-1](file:///d:/HocTap_TLU/ChuyenNganh_CNTT_AI/chuyendeKTPM/literareview/group-4-foundational-principles/md/dapper-2010-1.md) | Sigelman et al. (2010) | Distributed Tracing (Google Dapper) | Mục 2.5 & 2.8: Cơ chế Span/Trace Tree và chi phí hiệu năng của observability |

---

## 1. Tóm tắt chi tiết từng tài liệu

### 1.1. On the Criteria to be Used in Decomposing Systems into Modules / The Secret History of Information Hiding — David L. Parnas (1972 / ~2001)
- **Nguồn:** `On_the_Criteria_To_Be_Used_in_Decomposing_Systems.md` — David L. Parnas (McMaster University; bài gốc *CACM* 1972, bài hồi tưởng trích dẫn tới 2001).
- **Nguyên lý cốt lõi:**
  - **Information Hiding:** Phân rã hệ thống sao cho mọi quyết định thiết kế dễ thay đổi (*"secrets"*) được giấu sau abstract interfaces; interface chỉ bộc lộ các giả định bền vững (*"solid"*).
  - **Module độc lập với công cụ/tiến trình:** Module là một *work assignment* (đơn vị phân công công việc), không đồng nhất với class hay OS process. Gắn chặt module với process riêng gây **unnecessary overhead** khi không cần thực thi song song.
  - **Quan hệ `"uses"`:** Thay cho khái niệm mơ hồ *"levels of abstraction"*, Parnas dùng quan hệ `"uses"` giữa các chương trình để kiểm soát phụ thuộc không chu trình.
- **Cạm bẫy thực tế & Ý nghĩa cho đề tài:** Chia module theo luồng điều khiển (*flow-chart instinct*) hoặc phản ánh trực tiếp cấu trúc DB/tổ chức tạo ra interface xấu và coupling ngầm. Do đó, **Modular Monolith** có thể đạt tách biệt module chuẩn xác mà không tốn chi phí process/mạng; ngược lại **Microservices** nếu phân rã sai vẫn mắc *undesired coupling* qua mạng.

---

### 1.2. Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services — Gilbert & Lynch (2002)
- **Nguồn:** `GL-cap.md` — Seth Gilbert, Nancy Lynch (hình thức hóa bài giảng của Eric Brewer tại *PODC* 2000).
- **Nguyên lý cốt lõi (CAP Theorem):**
  - Hình thức hóa 3 tính chất: **Consistency** (*Atomic / Linearizable*), **Availability** (mọi request tới node không lỗi đều nhận response hữu hạn), và **Partition Tolerance** (chịu mất thông điệp tùy ý khi mạng phân mảnh).
  - **Theorem 1 & Corollary 1.1 (Asynchronous Network):** Bất khả thi để đạt đồng thời Atomic Consistency và Availability trong mạng bất đồng bộ khi có thể mất thông điệp (do không phân biệt được gói tin mất hay trễ vô hạn).
  - **Theorem 2 (Partially Synchronous Network):** Kể cả khi biết cận trên thời gian truyền/xử lý ($t_{msg}$, $t_{local}$), vẫn không thể đạt đồng thời cả hai nếu có mất gói tin.
  - **Theorem 4 ($t$-Connected Consistency):** Đề xuất mô hình nhất quán yếu có kiểm soát—trả về dữ liệu cũ (*stale data*) khi có partition và khôi phục nhất quán sau khi partition lành $> t$ thời gian.
- **Ý nghĩa cho đề tài:** **Modular Monolith** trên một DBMS tập trung nằm trong vùng **CA / single-node ACID** (không có partition mạng giữa các module). **Microservices** với dữ liệu phân tán bắt buộc đối mặt với network partition và phải chọn giữa **CP** (khóa phân tán/quorum, chấp nhận giảm availability khi sự cố) hoặc **AP** (chấp nhận eventual consistency / stale data).

---

### 1.3. Sagas — Hector Garcia-Molina & Kenneth Salem (1987)
- **Nguồn:** `38713.38742.md` — Hector Garcia-Molina, Kenneth Salem (Princeton University).
- **Nguyên lý cốt lõi:**
  - **Vấn đề của Long-Lived Transactions (LLTs):** Giữ lock DB lâu làm nghẽn transaction ngắn, tăng tỷ lệ abort khi crash và **tần suất deadlock tăng theo lũy thừa bậc 4 kích thước transaction** (trích Gray, 1981).
  - **Mô hình Saga:** Tách LLT thành chuỗi sub-transactions $T_1, T_2, \dots, T_n$ thực thi xen kẽ được; mỗi $T_i$ là một atomic transaction kèm một **Compensating Transaction ($C_i$)** để hoàn tác *về mặt ngữ nghĩa* (không khôi phục nguyên trạng vật lý vì các transaction khác đã xen vào). Hệ thống đảm bảo chạy đủ $T_1 \dots T_n$ hoặc chuỗi bù $T_1 \dots T_j, C_j \dots C_1$.
  - **Đánh đổi:** Nới lỏng **Isolation** (two-level nesting: kết quả trung gian bị nhìn thấy trước khi toàn bộ saga kết thúc); có thể dùng *Backward recovery* (chạy $C_i$) hoặc *Forward recovery* (dùng save-point).
- **Ý nghĩa cho đề tài:** Giải thích nguyên nhân gốc khiến Microservices phải dùng Saga thay cho giao dịch ACID xuyên dịch vụ, đồng thời làm rõ chi phí lập trình và độ phức tạp xử lý lỗi bù trừ.

---

### 1.4. AWS Prescriptive Guidance: Enabling Data Persistence in Microservices — Ward & Mohan (2021–2025)
- **Nguồn:** `modernization-data-persistence.md` — Tabby Ward & Balaji Mohan (AWS).
- **6 Patterns & Đánh đổi thực tế:**
  1. *Database-per-service:* Độc lập dữ liệu & polyglot persistence, nhưng khó query/transaction liên dịch vụ và chịu ràng buộc CAP.
  2. *API Composition:* Gọi nhiều service và thực hiện **in-memory join**; nhược điểm là **giảm availability tổng thể** khi chuỗi gọi dài và tăng lưu lượng mạng.
  3. *CQRS:* Tách đường đọc/ghi bất đồng bộ, phát sinh **eventual consistency**.
  4. *Event Sourcing:* Lưu chuỗi sự kiện để tái tạo trạng thái; tài liệu nhấn mạnh *bắt buộc kết hợp với Saga pattern* để giữ nhất quán liên dịch vụ.
  5. *Saga Pattern:* Điều phối qua sự kiện hoặc orchestrator (như Step Functions), nhưng **khó debug** và độ phức tạp tăng theo số dịch vụ.
  6. *Shared-database-per-service:* Nhiều service/module dùng chung một DB (hoặc tách private schemas/tables); giữ được ACID nhưng chịu **development-time coupling** (đổi schema) và **runtime coupling** (lock bảng nóng).
- **Ý nghĩa cho đề tài:** Đặt *Shared-database-per-service* (mô hình dữ liệu thường gặp của Modular Monolith) cạnh *Database-per-service* (Microservices) để đối chiếu trực tiếp đánh đổi ACID vs. Coupling/Operational Cost.

---

### 1.5. The Tail at Scale — Jeffrey Dean & Luiz André Barroso (2013)
- **Nguồn:** `TheTailAtScale.md` — Jeffrey Dean, Luiz André Barroso (*Communications of the ACM*, 2013).
- **Nguyên lý & Số liệu thực nghiệm:**
  - **Tail Latency Amplification:** Nếu một server có độ trễ trung bình 10 ms và **p99 = 1 s**, khi một request fan-out song song tới **100 servers** thì **63%** request người dùng sẽ mất $> 1\text{ s}$; nếu server đơn có tỷ lệ chậm $1/10.000$ mà fan-out tới **2.000 servers** thì gần **20% (~1/5)** request bị chậm. Trong cây fan-out thực tế tại Google, đợi 100% leaf xong có p99 = **140 ms** (gấp đôi mức xong 95% leaf = **70 ms**, dù 1 leaf ngẫu nhiên chỉ **10 ms**).
  - **Nguyên nhân biến thiên:** Chia sẻ CPU/cache/mạng, daemon nền, GC, queueing nhiều tầng, SSD GC (tăng độ trễ đọc 100 lần).
  - **Kỹ thuật giảm tail latency:** *Hedged requests* (trên BigTable đọc 1.000 keys/100 servers, gửi bản sao sau 10 ms giảm p99.9 từ **1.800 ms xuống 74 ms**, chỉ tăng **2%** tải); *Tied requests* (giảm p99 từ **67→42 ms (-37%)** trên cluster rỗi và **108→67 ms (-38%)** khi chạy chung TeraSort, overhead đĩa $< 1\%$); *Micro-partitions* và *Good-enough results*.
- **Ý nghĩa cho đề tài:** Giải thích vì sao trong **Microservices**, ngay cả khi độ trễ trung bình (p50) chấp nhận được, kiến trúc gọi phân tán/fan-out vẫn dễ khiến **p95 và p99 tăng vọt** so với lời gọi nội bộ trong **Modular Monolith**.

---

### 1.6. Dapper, a Large-Scale Distributed Systems Tracing Infrastructure — Sigelman et al. (2010)
- **Nguồn:** `dapper-2010-1.md` — Benjamin H. Sigelman et al. (Google).
- **Cơ chế & Số liệu overhead:**
  - Mô hình **Trace Tree & Spans** (`trace_id`, `span_id`, `parent_id` 64-bit) với thu thập *out-of-band* (ghi log cục bộ $\rightarrow$ daemon kéo về Bigtable; trung bình **426 bytes/span**, chiếm **<0,01%** lưu lượng mạng Google, CPU daemon **<0,3%** của 1 core).
  - Chi phí sinh span trên x86 2.2GHz: **204 ns** (root span), **176 ns** (non-root span), **9 ns** (annotation không sample).
  - **Ảnh hưởng hiệu năng thực tế trên Web search cluster:** Nếu trace 100% (`1/1` sampling), **độ trễ trung bình tăng +16,3%** và **throughput giảm -1,48%**; giảm xuống `1/16` thì latency chỉ tăng **+2,12%**, và `1/1024` gần như bằng 0 (**-0,20%**).
- **Ý nghĩa cho đề tài:** Chứng minh **Distributed Tracing** là bắt buộc trong Microservices để tìm bottleneck qua nhiều dịch vụ, nhưng bản thân công cụ observability này cũng tạo ra **chi phí hiệu năng và hạ tầng** đáng kể (một điểm cần tách bạch khi thiết kế thực nghiệm Chương 4).

---

## 2. Kết luận kiến thức tổng hợp cho Nhóm 4

6 công trình nền tảng này kết nối thành một **chuỗi nhân quả hoàn chỉnh** cho Chương 2:
1. **Ranh giới thiết kế (Parnas 1972):** Modularity là thuộc tính logic (*Information Hiding*), không đòi hỏi tách process. Modular Monolith giữ được tính module hóa mà không trả chi phí IPC/mạng.
2. **Dữ liệu & Giao dịch (CAP + Garcia-Molina & Salem + AWS):** Khi tách dữ liệu sang nhiều dịch vụ, Microservices bước vào vùng chi phối của CAP và bài toán LLT, buộc phải đánh đổi ACID lấy Eventual Consistency, Saga, CQRS và API Composition (giảm availability và tăng độ phức tạp debug).
3. **Hiệu năng đuôi (The Tail at Scale):** Giao tiếp qua mạng và fan-out giữa các microservice khuếch đại các dao động tài nguyên nhỏ thành độ trễ đuôi p95/p99 lớn.
4. **Chi phí quan sát (Dapper):** Để chẩn đoán được chuỗi gọi phân tán và độ trễ đuôi đó, Microservices cần hạ tầng Distributed Tracing, kéo theo cả chi phí vận hành lẫn overhead hiệu năng nếu tỷ lệ sampling cao.
