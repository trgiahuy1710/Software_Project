# 📘 Báo Cáo Dự Án Kỹ Thuật Phần Mềm

## Tên Dự Án: Xây dựng web app bán đồng phục bóng đá

## Nhóm Thực Hiện: Nhóm 10

## Giáo Viên Hướng Dẫn: Trịnh Thanh Bình

## Thời Gian Thực Hiện: 23/4/2025 – 18/6/2025

---

## 1. 🎯 Giới Thiệu

Dự án **"Xây dựng web app bán đồng phục bóng đá"** là một nền tảng thương mại điện tử được phát triển nhằm mục đích cung cấp các sản phẩm thời trang bóng đá chất lượng cao, giúp người hâm mộ dễ dàng tìm kiếm và mua sắm.

Dự án áp dụng mô hình phát triển phần mềm **Waterfall (thác nước)** để đảm bảo tiến trình phát triển có thứ tự, rõ ràng và dễ quản lý.

---

## 2. 🔁 Mô Hình Phát Triển: Waterfall

Mô hình Waterfall được áp dụng qua 5 giai đoạn chính của dự án:

### 2.1. Phân Tích Yêu Cầu (Requirement Analysis)

- Thu thập và phân tích yêu cầu từ người dùng để giải quyết các vấn đề như rào cản ngôn ngữ, thanh toán phức tạp của các trang web hiện có.  
- Xác định các chức năng chính:
  - Đăng nhập/Đăng ký người dùng.  
  - Hiển thị danh sách và chi tiết sản phẩm.  
  - Quản lý giỏ hàng và đặt hàng.  
  - Xử lý thanh toán (COD).  
  - Tìm kiếm sản phẩm.  
  - Admin quản lý sản phẩm (thêm, sửa, xóa).

### 2.2. Thiết Kế Hệ Thống (System Design)

- Thiết kế kiến trúc phần mềm: mô hình hóa hệ thống bằng biểu đồ Use‑Case và các biểu đồ tuần tự cho từng luồng chức năng.  
- Lựa chọn công nghệ:
  - **Backend**: Python, Flask.  
  - **Frontend**: HTML, CSS, JavaScript, Bootstrap.  
  - **CSDL**: SQLite.

### 2.3. Cài Đặt (Implementation)

- Phát triển frontend để xây dựng giao diện người dùng.  
- Phát triển backend để xử lý nghiệp vụ như quản lý người dùng, sản phẩm và đơn hàng.  
- Tích hợp cơ sở dữ liệu SQLite để lưu trữ thông tin.

### 2.4. Kiểm Thử (Testing)

- **Unit Test**: kiểm tra các hàm riêng lẻ như tính tổng giỏ hàng, xác thực đăng nhập.  
- **Integration Test**: kiểm tra sự phối hợp giữa các module (ví dụ: thêm sản phẩm vào giỏ và cập nhật cơ sở dữ liệu).  
- **System Test**: kiểm tra toàn bộ luồng chức năng.  
- **Acceptance Test**: đảm bảo phần mềm phù hợp với kỳ vọng người dùng.

### 2.5. Triển Khai (Deployment)

- Chuẩn bị môi trường hosting, cài đặt phần mềm cần thiết.  
- Triển khai mã nguồn, cấu hình bảo mật và tối ưu hóa.

### 2.6. Bảo Trì (Maintenance)

- Giám sát hệ thống, sửa lỗi phát sinh trong quá trình sử dụng.  
- Cập nhật tính năng mới dựa trên phản hồi người dùng và sao lưu dữ liệu định kỳ.

---

## 3. Phân Công Công Việc

| Thành viên | Mã Sinh Viên | Công việc phụ trách | Ghi chú |
|------------|--------------|---------------------|---------|
| Trịnh Gia Huy | 23010069 | Phát triển chức năng tìm kiếm, bảo mật, tài liệu hóa | Trưởng nhóm |
| Nguyễn Dương Tuấn Nguyên | 22010091 | Xây dựng trang chủ, tăng cường bảo mật và hiệu năng | Thành viên |
| Nguyễn Văn Lượng | 23010799 | Thiết kế giao diện, danh mục sản phẩm, chi tiết sản phẩm | Thành viên |
| Đào Anh Vũ | 23017197 | Tài khoản người dùng, giỏ hàng, thanh toán, kết nối CSDL | Thành viên |

### GitHub Profiles

- [@trgiahuy1710](https://github.com/trgiahuy1710)  
- [@Nguynef](https://github.com/Nguynef)  
- [@nvluong-05](https://github.com/nvluong-05)  
- [@VuDao381](https://github.com/VuDao381)

---

## 4. Kết Quả Đạt Được

- [x] Hoàn thành tài liệu phân tích yêu cầu hệ thống  
- [x] Hoàn thành thiết kế hệ thống với biểu đồ và giao diện đầy đủ  
- [x] Phát triển xong mã nguồn và các chức năng chính của web app  
- [x] Kiểm thử toàn bộ hệ thống và sửa lỗi  
- [x] Sản phẩm hoạt động ổn định, sẵn sàng triển khai

---

## 5. Khó Khăn & Giải Pháp

- **Khó khăn:** Cấu trúc mã nguồn ban đầu chưa theo chuẩn OOP.  
  **Giải pháp:** Tìm hiểu và học thêm về lập trình hướng đối tượng để cải thiện cấu trúc và tính bảo trì cho các phiên bản sau.
- **Khó khăn:** Giao diện người dùng (UI/UX) cần tinh chỉnh và làm đẹp hơn.  
  **Giải pháp:** Phát triển kỹ năng về React, Vue.js và các nguyên tắc UX/UI.
- **Khó khăn:** Thiếu kiến thức chuyên sâu về an ninh mạng.  
  **Giải pháp:** Học thêm các nguyên tắc bảo mật web và phòng ngừa lỗ hổng phổ biến.

---

## 6. Kết Luận

Dự án hoàn thành các mục tiêu cơ bản, xây dựng thành công trang web bán đồng phục bóng đá với các chức năng thiết yếu. Hệ thống hoạt động ổn định và đáp ứng nhu cầu ban đầu. Nhóm đã tích lũy được nhiều kiến thức và xác định hướng phát triển để nâng cao chất lượng sản phẩm.

---

## Lời cảm ơn

- [Flask documentation](https://flask.palletsprojects.com/en/3.0.x/)  
- [Bootstrap documentation](https://getbootstrap.com/docs)  
- [SQLite documentation](https://www.sqlite.org/docs.html)  
- [GitHub Python‑Flask community repositories](https://github.com/topics/python-flask-application)

## 🛠 Skills

Python, Flask, SQLite, JavaScript, HTML, CSS, Bootstrap
