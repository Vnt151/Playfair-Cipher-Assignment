# Playfair Cipher Assignment

## 📝 Mô tả dự án

Dự án thực hiện cài đặt thuật toán mã hóa cổ điển **Playfair Cipher** bằng ngôn ngữ lập trình **Python**. Đây là bài tập thực hành mật mã học tập trung vào việc xử lý ma trận khóa $5 \times 5$ và các quy tắc biến đổi cặp ký tự (digraphs).

## 🛠 Quy tắc cài đặt

* **Ma trận khóa**: Sử dụng ma trận kích thước **5x5**.
* **Bảng chữ cái**: Sử dụng 25 ký tự (chữ `J` được gộp chung với chữ `I`).
* **Tiền xử lý bản rõ (Plaintext)**:
* Loại bỏ toàn bộ khoảng trắng và ký tự đặc biệt.
* Tách thành các cặp 2 ký tự (digraphs).
* Chèn ký tự `X` nếu hai ký tự trong một cặp trùng nhau.
* Chèn ký tự `X` vào cuối nếu tổng số ký tự của chuỗi bị lẻ.



## 🚀 Ví dụ chạy thử (Test Case)

Chương trình được thiết lập sẵn ví dụ kiểm thử dựa trên dữ liệu từ buổi học:

* **Thông điệp gốc**: `DO YOU LIKE TO STUDY A CRYPTOGRAPHY COURSE`
* **Từ khóa (Key)**: `CRYPTO`
* **Kết quả**: Chương trình sẽ thực hiện mã hóa (Encryption) và giải mã (Decryption) ngược lại để kiểm tra tính chính xác.

## 📂 Cấu trúc thư mục

* `playfair.py`: Cài đặt thuật toán bằng Python.
* `README.md`: Hướng dẫn sử dụng và mô tả dự án.
* `.gitignore`: Cấu hình bỏ qua các file rác của hệ thống khi đẩy lên Git.

## 💻 Cách cài đặt và chạy

1. Đảm bảo bạn đã cài đặt **Python 3**.
2. Mở Terminal/PowerShell tại thư mục dự án.
3. Chạy lệnh:

```bash
python playfair.py
