# 📘 Báo Cáo Dự Án Kỹ Thuật Phần Mềm

## Tên Dự Án:
Xây dựng web app bán đồng phục bóng đá

## Nhóm Thực Hiện:
Nhóm 10

## Giáo Viên Hướng Dẫn:
Trịnh Thanh Bình

## Thời Gian Thực Hiện:
23/4/2025 – 18/6/2025

---

## 1. 🎯 Giới Thiệu

[cite_start]Dự án **"Xây dựng web app bán đồng phục bóng đá"** là một nền tảng thương mại điện tử được phát triển nhằm mục đích cung cấp các sản phẩm thời trang bóng đá chất lượng cao, giúp người hâm mộ dễ dàng tìm kiếm và mua sắm. [cite_start]Dự án áp dụng mô hình phát triển phần mềm **Waterfall (thác nước)** để đảm bảo tiến trình phát triển có thứ tự, rõ ràng và dễ quản lý.

---

## 2. 🔁 Mô Hình Phát Triển: Waterfall

Mô hình Waterfall được áp dụng qua 5 giai đoạn chính của dự án:

### 2.1. Phân Tích Yêu Cầu (Requirement Analysis)

* [cite_start]Thu thập và phân tích yêu cầu từ người dùng để giải quyết các vấn đề như rào cản ngôn ngữ, thanh toán phức tạp của các trang web hiện có.
* Xác định các chức năng chính:
    * [cite_start]Đăng nhập/Đăng ký người dùng.
    * [cite_start]Hiển thị danh sách và chi tiết sản phẩm.
    * [cite_start]Quản lý giỏ hàng và đặt hàng.
    * [cite_start]Xử lý thanh toán (COD).
    * [cite_start]Tìm kiếm sản phẩm.
    * [cite_start]Admin quản lý sản phẩm (thêm, sửa, xóa).

### 2.2. Thiết Kế Hệ Thống (System Design)

* [cite_start]Thiết kế kiến trúc phần mềm: Mô hình hóa hệ thống bằng biểu đồ Use-Case và các biểu đồ tuần tự cho từng luồng chức năng.
* Lựa chọn công nghệ:
    * [cite_start]**Backend**: Python, Flask.
    * [cite_start]**Frontend**: HTML, CSS, JavaScript, Bootstrap.
    * [cite_start]**CSDL**: SQLite.

### 2.3. Cài Đặt (Implementation)

* [cite_start]Phát triển frontend để xây dựng giao diện người dùng.
* [cite_start]Phát triển backend để xử lý các nghiệp vụ như quản lý người dùng, sản phẩm và đơn hàng.
* [cite_start]Tích hợp cơ sở dữ liệu SQLite để lưu trữ thông tin.

### 2.4. Kiểm Thử (Testing)

* [cite_start]**Kiểm thử đơn vị (Unit Test)**: Kiểm tra các hàm riêng lẻ như tính tổng giỏ hàng, xác thực đăng nhập.
* [cite_start]**Kiểm thử tích hợp (Integration Test)**: Kiểm tra sự phối hợp giữa các module, ví dụ như thêm sản phẩm vào giỏ và cập nhật CSDL.
* [cite_start]**Kiểm thử hệ thống (System Test)**: Kiểm tra toàn bộ luồng chức năng của hệ thống.
* [cite_start]**Kiểm thử chấp nhận (Acceptance Test)**: Đảm bảo phần mềm phù hợp với kỳ vọng của người dùng.

### 2.5. Triển Khai (Deployment)

* [cite_start]Chuẩn bị môi trường hosting, cài đặt các phần mềm cần thiết.
* [cite_start]Triển khai mã nguồn và cấu hình bảo mật, tối ưu hóa.

### 2.6. Bảo Trì (Maintenance)

* [cite_start]Giám sát hệ thống, sửa các lỗi phát sinh trong quá trình sử dụng.
* [cite_start]Cập nhật tính năng mới dựa trên phản hồi của người dùng và sao lưu dữ liệu định kỳ.

---

## 3. Phân Công Công Việc

| Thành viên | Mã Sinh Viên | Công việc phụ trách | Ghi chú |
| :--- | :--- | :--- | :--- |
| Trịnh Gia Huy | 23010069 | [cite_start]Phát triển chức năng tìm kiếm, bảo mật, tài liệu hóa  | Trưởng nhóm |
| Nguyễn Dương Tuấn Nguyên | 22010091 | [cite_start]Xây dựng trang chủ, tăng cường bảo mật và đảm bảo hiệu năng  | Thành viên |
| Nguyễn Văn Lượng | 23010799 | [cite_start]Thiết kế giao diện, danh mục sản phẩm, chi tiết sản phẩm  | Thành viên |
| Đào Anh Vũ | 23017197 | [cite_start]Xây dựng chức năng tài khoản người dùng, giỏ hàng, thanh toán, kết nối CSDL  | Thành viên |

## GitHub Profile

* [@trgiahuy1710](https://github.com/trgiahuy1710)
* [@Nguynef](https://github.com/Nguynef)
* [@nvluong-05](https://github.com/nvluong-05)
* [@VuDao381](https://github.com/VuDao381)

---

## 4. Kết Quả Đạt Được

* [cite_start][x] Hoàn thành tài liệu phân tích yêu cầu hệ thống 
* [cite_start][x] Hoàn thành thiết kế hệ thống với đầy đủ biểu đồ và giao diện 
* [cite_start][x] Hoàn thành mã nguồn và các chức năng chính của web app 
* [cite_start][x] Kiểm thử toàn bộ hệ thống và sửa lỗi 
* [cite_start][x] Sản phẩm hoạt động ổn định và sẵn sàng triển khai 

---

## 5. Khó Khăn & Giải Pháp

* [cite_start]**Khó khăn:** Cấu trúc mã nguồn ban đầu chưa theo chuẩn Lập trình hướng đối tượng (OOP).
    [cite_start]**→ Giải pháp:** Nhóm đã xác định cần tự tìm hiểu và học thêm về OOP để cải thiện cấu trúc và tính bảo trì của mã nguồn cho các phiên bản sau.
* [cite_start]**Khó khăn:** Giao diện người dùng (UI/UX) cần được hoàn thiện và làm đẹp mắt hơn.
    [cite_start]**→ Giải pháp:** Lên kế hoạch học thêm về các framework như React, Vue.js và các nguyên tắc thiết kế UX/UI để nâng cao trải nghiệm người dùng.
* [cite_start]**Khó khăn:** Cần nâng cao kiến thức về an ninh mạng để đảm bảo an toàn cho hệ thống.
    [cite_start]**→ Giải pháp:** Nhóm sẽ học thêm về các nguyên tắc bảo mật web và cách phòng ngừa các lỗ hổng phổ biến.

---

## 6. Kết Luận

[cite_start]Dự án đã hoàn tất các mục tiêu cơ bản, xây dựng thành công một trang web bán đồng phục bóng đá với các chức năng cần thiết. [cite_start]Hệ thống hoạt động ổn định và đáp ứng được nhu cầu ban đầu. [cite_start]Nhóm đã học hỏi được nhiều kiến thức và xác định các hướng phát triển tiếp theo để nâng cao chất lượng sản phẩm.

---

## Lời cảm ơn

-   [Flask documentation](https://flask.palletsprojects.com/en/3.0.x/)
-   [Bootstrap documentation](https://getbootstrap.com/docs)
-   [SQLite documentation](https://www.sqlite.org/docs.html)
-   [Github community’s repositories](https://github.com/topics/python-flask-application)

## 🛠 Skills
Python, Flask, SQLite, JavaScript, HTML, CSS, Bootstrap.
