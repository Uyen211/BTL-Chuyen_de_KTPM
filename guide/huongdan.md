Mình nghĩ hướng điều chỉnh của bạn là đúng, và thực ra đây là điểm rất quan trọng nếu muốn bài tập lớn có dáng dấp của một nghiên cứu khoa học thực sự.

Có một nguyên tắc mình muốn thống nhất trước:

**Không được biến giả định lý thuyết thành kết quả thực nghiệm, cũng không được biến nhận định chủ quan thành số liệu định lượng.**

Với đề tài này, mình đề xuất xây dựng báo cáo theo hướng **Literature-based Comparative Analysis + Controlled Experimental Evaluation** (phân tích so sánh dựa trên tài liệu nghiên cứu kết hợp đánh giá thực nghiệm có kiểm soát).

Điều đó có nghĩa:

- Phần lý thuyết: sử dụng sách chuyên khảo, bài báo khoa học, nghiên cứu thực nghiệm đã công bố và tài liệu kỹ thuật chính thức. Mọi con số được trích dẫn phải có nguồn, bối cảnh và điều kiện đo.
- Phần phân tích: tự tổng hợp, lập luận và so sánh dựa trên nguyên lý kiến trúc. Không tự chấm điểm 1–5 rồi vẽ biểu đồ radar như thể đó là kết quả khoa học.
- Phần thực nghiệm: tự xây dựng hai hệ thống tương đương, tự chạy kiểm thử và thu thập dữ liệu thực tế. Đây mới là nơi tạo ra bộ số liệu của nghiên cứu.
- Phần kết luận: đối chiếu kết quả thực nghiệm với những gì các nghiên cứu trước đã công bố, giải thích điểm tương đồng và khác biệt.

## **2. Cấu trúc báo cáo nghiên cứu khoa học đề xuất**

Mình không muốn chỉ đổi tên các chương trong tài liệu cũ. Mình muốn thiết kế lại logic nghiên cứu sao cho người đọc có thể lần theo một chuỗi lập luận:

**VẤN ĐỀ NGHIÊN CỨU**

Vì sao cần so sánh Modular Monolith và Microservices?

**CƠ SỞ LÝ THUYẾT**

Các nguyên lý và thuộc tính kiến trúc liên quan

**PHÂN TÍCH VÀ TỔNG HỢP NGHIÊN CỨU TRƯỚC**

Các nghiên cứu đã chứng minh điều gì? Còn điểm nào chưa rõ?

**THIẾT KẾ THỰC NGHIỆM**

Xây dựng hai phiên bản và xác định phương pháp đo

**KẾT QUẢ VÀ THẢO LUẬN**

Dữ liệu đo thực tế, kiểm định giả thuyết và đối chiếu nghiên cứu trước

**KẾT LUẬN**

Phạm vi áp dụng và khuyến nghị lựa chọn kiến trúc

Mình đề xuất cấu trúc chính thức gồm 6 chương.

### **CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI**

**1.1. Bối cảnh nghiên cứu**

- Sự phát triển của kiến trúc phần mềm trong các hệ thống backend.
- Sự phổ biến của Microservices và các vấn đề phát sinh khi áp dụng.
- Sự quan tâm trở lại đối với Modular Monolith.
- Nhu cầu đánh giá dựa trên bằng chứng thay vì quan niệm kiến trúc mới luôn tốt hơn.

**1.2. Vấn đề nghiên cứu**

Đặt ra vấn đề cốt lõi: Hai kiến trúc có cùng chức năng nghiệp vụ nhưng khác biệt về cấu trúc triển khai sẽ ảnh hưởng thế nào đến hiệu năng và chi phí vận hành?

**1.3. Mục tiêu nghiên cứu**

- Làm rõ nguyên lý thiết kế của hai kiến trúc.
- Phân tích các đánh đổi về thiết kế, dữ liệu, vận hành và hiệu năng.
- Tổng hợp bằng chứng từ các nghiên cứu đã công bố.
- Xây dựng hai phiên bản hệ thống có chức năng tương đương.
- Đánh giá bằng thực nghiệm có kiểm soát.

**1.4. Câu hỏi nghiên cứu**

| Mã  | Câu hỏi                                                            |
| --- | ------------------------------------------------------------------ |
| RQ1 | Hai kiến trúc khác nhau như thế nào về hiệu năng xử lý?            |
| RQ2 | Hai kiến trúc tiêu thụ tài nguyên phần cứng như thế nào?           |
| RQ3 | Sự khác biệt về quản lý dữ liệu và đảm bảo tính nhất quán là gì?   |
| RQ4 | Độ phức tạp triển khai, giám sát và bảo trì khác nhau như thế nào? |
| RQ5 | Trong những điều kiện nào mỗi kiến trúc thể hiện lợi thế?          |

**1.5. Đối tượng và phạm vi nghiên cứu**

**1.6. Phương pháp nghiên cứu**

- Nghiên cứu tài liệu (Literature Review).
- Phân tích và tổng hợp (Comparative Analysis).
- Thực nghiệm có kiểm soát (Controlled Experiment).
- Phân tích thống kê (Statistical Analysis).

**1.7. Đóng góp dự kiến và cấu trúc báo cáo.**

### **CHƯƠNG 2. CƠ SỞ LÝ THUYẾT**

Chương này không đơn thuần định nghĩa hai kiến trúc. Nó phải giải thích các nguyên lý nền tảng khiến chúng có cách hoạt động khác nhau.

**2.1. Tổng quan kiến trúc phần mềm**

- Khái niệm Software Architecture.
- Architectural Styles và Architectural Patterns.
- Quality Attributes.
- Các thuộc tính liên quan: Performance, Scalability, Modifiability, Availability, Reliability, Deployability.

**2.2. Nguyên lý thiết kế hệ thống module**

- Modularity.
- Information Hiding.
- Separation of Concerns.
- High Cohesion và Low Coupling.
- Domain-Driven Design và Bounded Context.
- Nguyên lý phân chia hệ thống theo miền nghiệp vụ.

**2.3. Kiến trúc Modular Monolith**

- Định nghĩa và đặc trưng.
- Cấu trúc module và public interface.
- Module Boundary và Dependency Management.
- Giao tiếp nội bộ giữa các module.
- Quản lý dữ liệu giữa các module.
- Kiểm soát sự phụ thuộc và bảo vệ tính module hóa.

**2.4. Kiến trúc Microservices**

- Định nghĩa và đặc trưng.
- Service Independence.
- Independent Deployment.
- Database per Service.
- Giao tiếp đồng bộ và bất đồng bộ.
- Service Discovery, API Gateway, Message Broker.
- Containerization và Orchestration.

**2.5. Các nguyên lý của hệ thống phân tán**

Đây là mục rất quan trọng vì nó giải thích những chi phí phát sinh khi chuyển từ lời gọi nội bộ sang giao tiếp mạng.

- Network Latency.
- Partial Failure.
- Network Partition.
- Serialization và Deserialization.
- Timeout, Retry, Circuit Breaker.
- Fault Isolation và Bulkhead.
- Distributed Tracing.

**2.6. Quản lý giao dịch và tính nhất quán dữ liệu**

- ACID và BASE.
- CAP Theorem.
- Strong Consistency và Eventual Consistency.
- Distributed Transactions.
- Saga Pattern.
- Transactional Outbox.
- Idempotency.

**2.7. Các nguyên lý và chỉ số đánh giá hiệu năng**

- Latency và Percentile (p50, p95, p99).
- Throughput.
- CPU Utilization và Memory Consumption.
- Little's Law.
- Queueing Theory.
- Tail Latency.
- Load Testing: Open Model và Closed Model.

**2.8. Nguyên lý vận hành và quản lý hệ thống**

- Continuous Integration và Continuous Delivery.
- Infrastructure as Code.
- Logging, Monitoring và Observability.
- DORA Metrics.
- Incident Management và Fault Diagnosis.

### **CHƯƠNG 3. TỔNG QUAN NGHIÊN CỨU VÀ PHÂN TÍCH SO SÁNH**

Đây là chương mình muốn bạn đầu tư nhiều nhất vào chất lượng lập luận. Nó là cầu nối giữa lý thuyết và thực nghiệm.

**3.1. Tổng quan các nghiên cứu liên quan**

- Các nghiên cứu so sánh hiệu năng Monolith và Microservices.
- Các nghiên cứu về khả năng mở rộng.
- Các nghiên cứu về chi phí vận hành.
- Các nghiên cứu về Modular Monolith.
- Tổng hợp những kết quả và giới hạn của nghiên cứu trước.

**3.2. So sánh về thiết kế và cấu trúc hệ thống**

- Ranh giới module và ranh giới dịch vụ.
- Mức độ phụ thuộc giữa các thành phần.
- Khả năng thay đổi và mở rộng chức năng.
- Khả năng phát triển độc lập.
- Khả năng mở rộng quy mô đội ngũ.

**3.3. So sánh về tính toàn vẹn và nhất quán dữ liệu**

- Giao dịch ACID trong cùng tiến trình.
- Database per Service.
- Giao dịch phân tán.
- Saga và cơ chế bù trừ.
- Eventual Consistency.
- Các rủi ro phát sinh khi hệ thống gặp sự cố.

**3.4. So sánh về độ phức tạp vận hành**

- Cấu trúc triển khai và quản lý hạ tầng.
- CI/CD và quy trình phát hành.
- Monitoring, Logging và Distributed Tracing.
- Quản lý lỗi và khả năng khôi phục.
- Khả năng chẩn đoán sự cố.
- Gánh nặng cấu hình và bảo trì.

**3.5. So sánh về hiệu năng và sử dụng tài nguyên**

- Chi phí giao tiếp nội bộ so với giao tiếp mạng.
- Chi phí serialization/deserialization.
- Ảnh hưởng của số lượng dịch vụ trong một luồng nghiệp vụ.
- Ảnh hưởng của tải đồng đều và tải không đồng đều.
- Khả năng mở rộng ngang và mở rộng dọc.
- Mức tiêu thụ CPU, RAM và tài nguyên mạng.

**3.6. Tổng hợp kết quả từ các nghiên cứu trước**

Đây phải là một bảng tổng hợp nghiên cứu thực nghiệm thực sự, không phải bảng tự chấm điểm.

| Nghiên cứu               | Phương pháp                       | Chỉ số đánh giá                         | Kết quả chính                                           | Hạn chế                           |
| ------------------------ | --------------------------------- | --------------------------------------- | ------------------------------------------------------- | --------------------------------- |
| Blinowski et al. (2022)  | Thực nghiệm có kiểm soát          | Performance, Scalability                | Monolith tốt hơn trên một máy trong bối cảnh nghiên cứu | Phụ thuộc môi trường và công nghệ |
| Villamizar et al. (2015) | Đánh giá triển khai trên cloud    | Hiệu năng, chi phí                      | Phân tích ảnh hưởng của chiến lược triển khai           | Điều kiện triển khai cụ thể       |
| Su & Li (2024)           | Systematic Grey Literature Review | Cấu trúc, framework, trường hợp thực tế | Hệ thống hóa khái niệm Modular Monolith                 | Không phải benchmark hiệu năng    |

**3.7. Khoảng trống nghiên cứu (Research Gap)**

- Thiếu các nghiên cứu đối chiếu trực tiếp Modular Monolith và Microservices trong cùng một nghiệp vụ, cùng điều kiện tài nguyên.
- Hiệu năng thường được đánh giá riêng lẻ, chưa đồng thời xét đến độ phức tạp vận hành.
- Nhiều nghiên cứu chỉ đánh giá khả năng mở rộng mà chưa làm rõ chi phí phát sinh.
- Kết quả phụ thuộc mạnh vào công nghệ, cấu hình và môi trường triển khai.

Lưu ý: Đây là các hướng khoảng trống cần được kiểm chứng qua quá trình rà soát tài liệu, không nên tuyên bố chúng là sự thật tuyệt đối trước khi hoàn thành tổng quan nghiên cứu.

**3.8. Đề xuất mô hình phân tích và giả thuyết nghiên cứu**

Ví dụ:

- H1: Modular Monolith có độ trễ thấp hơn Microservices trong điều kiện chạy trên cùng một máy và cùng giới hạn tài nguyên.
- H2: Microservices có chi phí tài nguyên nền cao hơn khi số lượng dịch vụ và thành phần hạ tầng tăng.
- H3: Modular Monolith có độ phức tạp triển khai thấp hơn.
- H4: Microservices có lợi thế về khả năng mở rộng chọn lọc khi tải giữa các miền nghiệp vụ không đồng đều.
- H5: Microservices phát sinh thêm chi phí đảm bảo tính nhất quán dữ liệu trong các giao dịch xuyên dịch vụ.

Các giả thuyết này không phải kết quả đã được chứng minh. Chúng là những dự đoán cần kiểm định.

### **CHƯƠNG 4. THIẾT KẾ VÀ TRIỂN KHAI THỰC NGHIỆM**

**4.1. Mục tiêu và phương pháp thực nghiệm**

**4.2. Thiết kế nghiệp vụ mẫu**

- Mô tả nghiệp vụ xử lý đơn hàng.
- Các thành phần Order, Inventory, Payment, Notification.
- Luồng xử lý thành công và thất bại.
- Xác định hợp đồng chức năng chung.

**4.3. Thiết kế kiến trúc thực nghiệm**

- Thiết kế Modular Monolith.
- Thiết kế Microservices.
- Sơ đồ thành phần.
- Sơ đồ luồng dữ liệu và tương tác.
- Thiết kế cơ sở dữ liệu.

**4.4. Công nghệ và môi trường triển khai**

- Ngôn ngữ lập trình và framework.
- Database.
- Docker và Docker Compose.
- k6.
- Prometheus và Grafana.
- Cấu hình CPU, RAM, hệ điều hành.

**4.5. Thiết kế kịch bản kiểm thử**

- Kiểm thử tải thấp, trung bình và cao.
- Stress Testing.
- Spike Testing.
- Fault Injection.
- Kiểm thử khả năng mở rộng nếu môi trường cho phép.

**4.6. Các chỉ số đánh giá**

- Latency: p50, p95, p99.
- Throughput: requests/second.
- Error Rate.
- CPU Utilization.
- Memory Consumption.
- Resource Consumption per Request.

**4.7. Phương pháp đo độ phức tạp vận hành**

- Số lượng thành phần triển khai.
- Số lượng cấu hình và pipeline.
- Thời gian build và deploy.
- Thời gian dựng môi trường.
- Thời gian phát hiện và chẩn đoán lỗi.
- Khối lượng cấu hình và mã nguồn hạ tầng.

**4.8. Phương pháp xử lý dữ liệu và kiểm định giả thuyết**

**4.9. Các mối đe dọa đến tính hợp lệ của thực nghiệm.**

### **CHƯƠNG 5. KẾT QUẢ THỰC NGHIỆM VÀ THẢO LUẬN**

Đây là chương chỉ được viết sau khi có dữ liệu đo thực tế.

**5.1. Kết quả kiểm thử hiệu năng**

**5.2. Kết quả đo mức tiêu thụ tài nguyên**

**5.3. Kết quả đánh giá độ phức tạp vận hành**

**5.4. Kết quả kiểm thử khi có sự cố**

**5.5. Phân tích và kiểm định giả thuyết**

**5.6. Đối chiếu kết quả với các nghiên cứu trước**

**5.7. Thảo luận về ưu điểm, nhược điểm và phạm vi áp dụng của từng kiến trúc.**

### **CHƯƠNG 6. KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN**

- Tổng kết kết quả nghiên cứu.
- Trả lời các câu hỏi nghiên cứu.
- Những đóng góp của đề tài.
- Hạn chế nghiên cứu.
- Hướng phát triển tiếp theo.

## **4. Cách sử dụng số liệu từ các paper mà không biến báo cáo thành nơi chép số liệu**

Đây là phần mình muốn nhấn mạnh nhất.

Bạn không nên chỉ tìm một paper, lấy con số của họ rồi đưa vào biểu đồ của mình. Số liệu nghiên cứu luôn gắn với điều kiện thực nghiệm.

Ví dụ, paper Blinowski et al. (2022) cho thấy Monolith hoạt động tốt hơn Microservices trên một máy trong môi trường thử nghiệm của họ. Nhưng không thể từ đó kết luận Monolith luôn nhanh hơn Microservices.&#x20;

Mình đề xuất một quy trình khai thác tài liệu như sau.

### **4.1. Phân loại bằng chứng**

| Loại bằng chứng                | Cách sử dụng                                           |
| ------------------------------ | ------------------------------------------------------ |
| Nguyên lý lý thuyết            | Giải thích cơ chế và bản chất kiến trúc                |
| Kết quả thực nghiệm từ paper   | Trích dẫn số liệu, điều kiện và kết quả                |
| Case study thực tế             | Minh chứng cho quyết định kiến trúc trong doanh nghiệp |
| Khảo sát chuyên gia            | Minh chứng cho những khó khăn trong thực tế            |
| Nhận định của người nghiên cứu | Phân tích và suy luận, phải ghi rõ đây là nhận định    |

### **4.2. Xây dựng bảng tổng hợp bằng chứng**

Mình muốn bạn có một bảng riêng trong quá trình nghiên cứu, ví dụ:

| Paper                    | Thông số được trích xuất       | Điều kiện đo           | Ý nghĩa đối với đề tài                    |
| ------------------------ | ------------------------------ | ---------------------- | ----------------------------------------- |
| Blinowski et al. (2022)  | Latency, scalability           | Local, Azure           | So sánh hiệu năng và ảnh hưởng môi trường |
| Villamizar et al. (2015) | Performance, deployment cost   | Cloud                  | Phân tích triển khai                      |
| JSS (2021)               | Monitoring, testing challenges | Survey + interviews    | Độ phức tạp vận hành                      |
| Su & Li (2024)           | 64 tài liệu được lựa chọn      | Grey literature review | Cơ sở về Modular Monolith                 |

Khi đọc từng paper, hãy thu thập thêm:

- Hardware configuration.
- Software stack.
- Workload.
- Number of users/concurrent requests.
- Measurement methodology.
- Baseline architecture.
- Experimental results.
- Limitations.

**Không có điều kiện đo thì không nên trích dẫn một con số như bằng chứng so sánh.**

### **4.3. Những biểu đồ nên xuất hiện trong Chương 3**

Mình đề xuất chỉ sử dụng ba dạng trực quan:

1. Sơ đồ nguyên lý: minh họa sự khác biệt trong cơ chế hoạt động.
2. Bảng tổng hợp nghiên cứu: đối chiếu các kết quả đã công bố.
3. Biểu đồ số liệu từ paper: chỉ sử dụng khi trích xuất được dữ liệu thực và có thể ghi rõ nguồn, điều kiện đo.

Không cần biểu đồ radar, không cần bản đồ nhiệt tự chấm điểm, không cần biểu đồ giả lập chỉ để làm báo cáo trông có vẻ định lượng.

## **5. Một số vấn đề phương pháp nghiên cứu cần chốt trước khi bắt tay viết**

Có ba điểm mình muốn chất vấn thiết kế ban đầu của bạn.

### **5.1. Modular Monolith và Microservices có thực sự được so sánh công bằng?**

Bạn cần phân biệt hai loại so sánh:

- **So sánh kiến trúc trong cùng tài nguyên:** Cấp cùng giới hạn CPU/RAM, chạy trên cùng máy. Mục tiêu là đo chi phí của cách tổ chức và giao tiếp.
- **So sánh khả năng mở rộng:** Cho phép mỗi kiến trúc mở rộng tài nguyên theo cách phù hợp với nó. Mục tiêu là đo khả năng đáp ứng khi tải tăng.

Nếu chỉ thực nghiệm trên một máy duy nhất, bạn chỉ có thể kết luận về hiệu năng trong môi trường một máy. Bạn không thể dùng kết quả đó để kết luận Microservices không có lợi thế mở rộng ngang.

Mình đề xuất chia thành hai chế độ:

| Chế độ                  | Điều kiện                     | Mục tiêu                         |
| ----------------------- | ----------------------------- | -------------------------------- |
| E1 – Resource Parity    | Cùng giới hạn tài nguyên      | So sánh hiệu năng và chi phí nền |
| E2 – Scaling Evaluation | Cho phép thay đổi số instance | So sánh khả năng mở rộng         |

E2 có thể là phần mở rộng nếu thời gian và hạ tầng không cho phép thực hiện đầy đủ.

### **5.2. Có nên đưa độ phức tạp vận hành vào cùng một thước đo?**

Không nên cộng số lượng container, số dòng cấu hình và thời gian triển khai thành một điểm số tổng hợp tùy ý.

Hãy giữ từng chỉ số độc lập.

Ví dụ:

- Deployment Complexity: số đơn vị triển khai và cấu hình.
- Deployment Time: thời gian triển khai.
- Environment Setup Time: thời gian dựng môi trường.
- Fault Diagnosis Time: thời gian tìm nguyên nhân lỗi.
- Change Propagation: số module/dịch vụ phải thay đổi khi bổ sung chức năng.

Như vậy, kết quả sẽ minh bạch và có khả năng tái lập hơn.

### **5.3. Không nên làm cho hai kiến trúc khác biệt quá nhiều về công nghệ**

Ví dụ, nếu Modular Monolith sử dụng PostgreSQL nhưng Microservices lại dùng PostgreSQL + Redis + RabbitMQ + Kafka, bạn sẽ khó xác định sự khác biệt hiệu năng đến từ kiến trúc hay từ công nghệ bổ sung.

Hãy thiết kế hai phiên bản tương đương về:

- Nghiệp vụ.
- Ngôn ngữ và framework.
- Logic xử lý.
- Dữ liệu đầu vào.
- Cấu hình tài nguyên.
- Chính sách cache và các cơ chế tối ưu.

Những thành phần bắt buộc phát sinh do kiến trúc Microservices phải được ghi nhận riêng và tính vào chi phí vận hành.

## **6. Thứ tự triển khai nghiên cứu mình đề xuất**

Đừng vội viết 6 chương ngay. Nếu làm vậy, bạn rất dễ quay lại tình trạng viết trước rồi đi tìm paper để hợp thức hóa những gì đã viết.

Mình muốn bạn đi theo thứ tự sau:

1. **Giai đoạn 1 – Xây dựng bộ tài liệu nghiên cứu**

   Làm trước

   Đọc 8 paper ưu tiên ở trên. Thu thập kết quả, phương pháp, hạn chế và thông tin trích dẫn.
2. **Giai đoạn 2 – Xây dựng khung lý thuyết**

   Viết Chương 2, mỗi nguyên lý đều phải trả lời được câu hỏi: Nó ảnh hưởng thế nào đến hai kiến trúc?
3. **Giai đoạn 3 – Tổng hợp và phân tích**

   Viết Chương 3, đối chiếu các paper, phân tích trade-off, xác định research gap và đưa ra giả thuyết.
4. **Giai đoạn 4 – Thiết kế thực nghiệm**

   Chốt nghiệp vụ, kiến trúc, công nghệ, biến độc lập, biến phụ thuộc và phương pháp kiểm thử.
5. **Giai đoạn 5 – Triển khai và đánh giá**

   Xây dựng hai hệ thống, chạy k6, thu thập dữ liệu, xử lý thống kê.
6. **Giai đoạn 6 – Hoàn thiện báo cáo**

   Viết kết quả, thảo luận, đối chiếu nghiên cứu trước và kết luận.

## **7. Kết luận định hướng**

Mình muốn bài nghiên cứu này có ba tầng giá trị:

1. **Theoretical Foundation:** Hiểu được bản chất của hai kiến trúc thông qua các nguyên lý kỹ thuật phần mềm và hệ thống phân tán.
2. **Evidence-based Comparison:** Có bằng chứng từ các công trình nghiên cứu trước, không dựa trên nhận định cảm tính.
3. **Experimental Validation:** Tự triển khai, tự đo và kiểm chứng các giả thuyết trong điều kiện được kiểm soát.

Một lưu ý học thuật: vì đề tài của bạn đặt trọng tâm vào Modular Monolith, hãy đặc biệt chú ý paper của Su & Li (2024) và nghiên cứu năm 2025 về so sánh trực tiếp Modular Monolith với Microservices. Đừng để phần nghiên cứu biến thành một bài so sánh Monolith truyền thống với Microservices rồi chỉ đổi tên Monolith thành Modular Monolith.

**Bước tiếp theo mình đề xuất:** Chúng ta nên xây dựng một *Research Matrix* cho toàn bộ đề tài, tức bảng liên kết giữa từng mục trong 6 chương, câu hỏi cần trả lời, paper nguồn, bằng chứng cần trích xuất và loại lập luận được phép sử dụng. Đây sẽ là bộ khung kiểm soát chất lượng học thuật trước khi bạn bắt đầu viết báo cáo chính thức.