# Nghiên cứu, Đánh giá Thực nghiệm Hiệu năng và Độ phức tạp Vận hành giữa Modular Monolith và Microservices

Repository lưu trữ toàn bộ tài liệu nghiên cứu lý thuyết, tổng quan tài liệu khoa học (*Literature Review*), thiết kế thực nghiệm và mã nguồn kiểm thử tải cho bài tập lớn môn **Chuyên đề Kỹ thuật Phần mềm**.

## Cấu trúc thư mục

- `docs/` — Báo cáo nghiên cứu và tài liệu kiểm soát chất lượng học thuật:
  - [evidence_table.md](docs/evidence_table.md): Bảng trích xuất bằng chứng từ 20 tài liệu khoa học (gắn điều kiện đo).
  - [research_matrix.md](docs/research_matrix.md): Ma trận liên kết 6 chương báo cáo với câu hỏi nghiên cứu (`RQ1`–`RQ5`).
  - [chuong_1_gioi_thieu_de_tai.md](docs/chuong_1_gioi_thieu_de_tai.md): Chương 1 — Giới thiệu đề tài.
  - [chuong_2_co_so_ly_thuyet.md](docs/chuong_2_co_so_ly_thuyet.md): Chương 2 — Cơ sở lý thuyết.
  - [chuong_3_tong_quan_va_phan_tich_so_sanh.md](docs/chuong_3_tong_quan_va_phan_tich_so_sanh.md): Chương 3 — Tổng quan nghiên cứu & phân tích so sánh (kèm 5 biểu đồ tại `docs/figures/`).
  - [chuong_4_thiet_ke_thuc_nghiem.md](docs/chuong_4_thiet_ke_thuc_nghiem.md): Chương 4 — Thiết kế và triển khai thực nghiệm.
- `literareview/` — 20 bài báo khoa học (`.md` & `.pdf`) phân thành 4 nhóm chuyên đề kèm `literature_review.md` cho từng nhóm.
- `scripts/` — Script Python (`matplotlib`/`numpy`) sinh biểu đồ từ dữ liệu thực nghiệm công bố.
- `experiments/` — Mã nguồn hai hệ thống đối chứng (`modular-monolith/`, `microservices/`), kịch bản tải `k6/`, cấu hình giám sát `Prometheus/Grafana` và dữ liệu đo.
- `process/` — Kế hoạch triển khai kỹ thuật theo chuẩn `vc-plan-agent`.
- `guide/` — Tài liệu định hướng phương pháp luận và quy chuẩn văn phong học thuật.

## Tiến độ hiện tại

- [x] **Giai đoạn 0–1:** Phân nhóm 20 bài báo, lập Literature Review, Evidence Table và Research Matrix.
- [x] **Giai đoạn 2–3:** Hoàn thành nghiên cứu lý thuyết (Chương 1, Chương 2, Chương 3 + 5 biểu đồ số liệu thực).
- [x] **Giai đoạn 4:** Chốt thiết kế thực nghiệm có kiểm soát (Chương 4).
- [ ] **Giai đoạn 5–6:** Triển khai mã nguồn thực nghiệm trong `experiments/`, chạy `k6`, thu thập số liệu và hoàn thiện Chương 5–6.
