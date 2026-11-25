# CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI

## 1.1. Bối cảnh Nghiên cứu

Trong hơn một thập kỷ qua, **Kiến trúc Vi dịch vụ (Microservices Architecture - MSA)** đã trở thành lựa chọn phổ biến trong phát triển các hệ thống *backend* nhờ khả năng phân tách dịch vụ độc lập, tự do lựa chọn công nghệ và mở rộng linh hoạt theo từng thành phần. Tuy nhiên, quá trình áp dụng rộng rãi trong công nghiệp cũng bộc lộ hàng loạt chi phí ẩn về hạ tầng, quản lý dữ liệu phân tán, kiểm thử tích hợp và giám sát vận hành (Soldani và các cộng sự, 2018; Waseem và các cộng sự, 2021). Thực tế này thúc đẩy sự quan tâm trở lại đối với **Kiến trúc Nguyên khối Mô-đun hóa (Modular Monolith)** — mô hình giữ nguyên đơn vị triển khai thống nhất nhưng áp đặt ranh giới mô-đun chặt chẽ theo miền nghiệp vụ, được nhiều doanh nghiệp quy mô lớn như Shopify, Appsmith hay Gusto lựa chọn (Su và Li, 2024).

Trước hai xu hướng trái ngược đó, việc lựa chọn kiến trúc không thể dựa trên trào lưu công nghệ hay quan niệm mặc định rằng kiến trúc phân tán luôn ưu việt hơn, mà đòi hỏi những đánh giá dựa trên bằng chứng thực nghiệm có kiểm soát.

## 1.2. Vấn đề Nghiên cứu

Vấn đề cốt lõi của đề tài được đặt ra như sau: *Khi hai hệ thống phần mềm thực thi cùng một tập chức năng nghiệp vụ, sử dụng cùng ngăn xếp công nghệ và nền tảng triển khai, nhưng khác biệt về cấu trúc kiến trúc (Modular Monolith so với Microservices), sự khác biệt đó sẽ tác động như thế nào đến hiệu năng xử lý, mức tiêu thụ tài nguyên phần cứng và độ phức tạp vận hành?*

## 1.3. Mục tiêu Nghiên cứu

Để giải quyết vấn đề trên một cách có hệ thống, nghiên cứu hướng tới năm mục tiêu cụ thể:
1. Làm rõ các nguyên lý thiết kế phần mềm và hệ thống phân tán chi phối cơ chế hoạt động của Modular Monolith và Microservices.
2. Phân tích toàn diện sự đánh đổi giữa hai kiến trúc trên bốn khía cạnh: thiết kế cấu trúc, tính toàn vẹn dữ liệu, độ phức tạp vận hành và hiệu năng xử lý.
3. Tổng hợp và đối chiếu có điều kiện các bằng chứng định lượng, khảo sát chuyên gia và nghiên cứu trường hợp từ các công trình khoa học đã công bố.
4. Thiết kế và xây dựng hai phiên bản hệ thống xử lý đơn hàng có chức năng nghiệp vụ tương đương theo kiến trúc Modular Monolith và Microservices.
5. Tiến hành đánh giá thực nghiệm có kiểm soát (kiểm thử tải, đo tài nguyên và định lượng chỉ số vận hành độc lập) để kiểm định các giả thuyết nghiên cứu.

## 1.4. Câu hỏi Nghiên cứu

Nghiên cứu tập trung trả lời năm câu hỏi nghiên cứu (*Research Questions - RQ*) sau đây:

| Mã | Câu hỏi nghiên cứu |
| :---: | :--- |
| **RQ1** | Hai kiến trúc Modular Monolith và Microservices khác nhau như thế nào về hiệu năng xử lý (độ trễ theo phân vị `p50`/`p95`/`p99`, thông lượng `RPS` và tỷ lệ lỗi)? |
| **RQ2** | Hai kiến trúc tiêu thụ tài nguyên phần cứng (CPU, RAM và tài nguyên trên mỗi yêu cầu) khác nhau như thế nào dưới cùng giới hạn tài nguyên? |
| **RQ3** | Sự khác biệt về quản lý dữ liệu, giao dịch liên thành phần và cơ chế đảm bảo tính nhất quán giữa hai kiến trúc là gì? |
| **RQ4** | Độ phức tạp triển khai, cấu hình, giám sát và chẩn đoán sự cố giữa hai kiến trúc khác nhau như thế nào khi đo bằng các chỉ số vận hành độc lập? |
| **RQ5** | Trong những điều kiện cụ thể nào (giới hạn tài nguyên trên một nút, tải đồng đều hay không đồng đều, yêu cầu mở rộng chọn lọc) mỗi kiến trúc thể hiện lợi thế rõ rệt? |

## 1.5. Đối tượng và Phạm vi Nghiên cứu

- **Đối tượng nghiên cứu:** Kiến trúc Modular Monolith (tổ chức mô-đun nghiệp vụ với ranh giới giao diện tường minh trong một tiến trình duy nhất) và kiến trúc Microservices (phân tách dịch vụ độc lập theo mô hình *Database per Service*, giao tiếp qua mạng và điều phối bằng container).
- **Phạm vi lý thuyết và tổng quan:** Tập trung vào các nguyên lý thiết kế mô-đun, hệ thống phân tán, quản lý dữ liệu/giao dịch, hiệu năng và vận hành dựa trên tập 20 tài liệu khoa học và kỹ thuật đã tuyển chọn.
- **Phạm vi thực nghiệm:** Xây dựng một luồng nghiệp vụ xử lý đơn hàng mẫu (`Order`, `Inventory`, `Payment`, `Notification`) trên cùng ngăn xếp công nghệ và triển khai qua Docker Compose. Thực nghiệm tập trung vào chế độ đối sánh công bằng về tài nguyên trên một nút (`E1 – Resource Parity`) và khảo sát khả năng mở rộng chọn lọc (`E2 – Scaling Evaluation` trong giới hạn hạ tầng cho phép), không mở rộng sang cụm đa vùng địa lý (*multi-region cloud*) quy mô lớn.

## 1.6. Phương pháp Nghiên cứu

Đề tài áp dụng phương pháp **Phân tích so sánh dựa trên tài liệu kết hợp Đánh giá thực nghiệm có kiểm soát (*Literature-based Comparative Analysis + Controlled Experimental Evaluation*)**, gồm bốn bước:
1. **Nghiên cứu tài liệu (*Literature Review*):** Khai thác có hệ thống 20 công trình khoa học và tài liệu kỹ thuật, trích xuất bằng chứng gắn chặt với điều kiện đo để tránh tách rời số liệu khỏi bối cảnh.
2. **Phân tích và tổng hợp (*Comparative Analysis*):** Đối chiếu cơ chế kiến trúc theo từng thuộc tính chất lượng, xác định khoảng trống nghiên cứu và thiết lập hệ giả thuyết $H_1 \dots H_5$.
3. **Thực nghiệm có kiểm soát (*Controlled Experiment*):** Khóa chặt các biến gây nhiễu (*tech-stack parity*, *deployment parity*, *resource parity*), sử dụng `k6` để tạo tải và `Prometheus/Grafana` kết hợp thu thập số liệu Docker để đo đạc tự động.
4. **Phân tích thống kê (*Statistical Analysis*):** Chạy lặp lại nhiều lần các kịch bản kiểm thử và kiểm định ý nghĩa thống kê của sự khác biệt trước khi đối chiếu với các công trình đi trước.

## 1.7. Đóng góp Dự kiến và Cấu trúc Báo cáo

Đóng góp dự kiến của đề tài nằm ở hai điểm: (1) hệ thống hóa ranh giới khác biệt giữa **Modular Monolith** (thay vì Monolith truyền thống) và **Microservices** dựa trên bằng chứng khoa học có kiểm chứng; và (2) cung cấp bộ dữ liệu thực nghiệm tái lập được trong điều kiện cân bằng tài nguyên Docker, kết hợp đồng thời các chỉ số hiệu năng đuôi (`p95`/`p99`), mức tiêu thụ RAM/CPU và bộ chỉ số độ phức tạp vận hành độc lập.

Phần còn lại của báo cáo được tổ chức thành năm chương tiếp theo: **Chương 2** trình bày cơ sở lý thuyết nền tảng; **Chương 3** tổng quan các nghiên cứu liên quan, phân tích so sánh và đề xuất giả thuyết; **Chương 4** mô tả chi tiết thiết kế hệ thống và phương pháp thực nghiệm; **Chương 5** trình bày kết quả đo thực tế và thảo luận; và **Chương 6** tổng kết câu trả lời cho `RQ1`–`RQ5` cùng hướng phát triển.
