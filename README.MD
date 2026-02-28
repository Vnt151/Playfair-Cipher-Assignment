Thuật toán Playfair Cipher (Python)
Dự án này thực hiện cài đặt thuật toán mã hóa cổ điển Playfair Cipher bằng ngôn ngữ lập trình Python. Đây là bài tập thực hành thuộc môn An toàn thông tin, tập trung vào việc xử lý ma trận và các quy tắc thay thế cặp ký tự (digraph).

📌 Các quy tắc áp dụng
Hệ thống tuân thủ các quy tắc chuẩn của mật mã học Playfair:

Ma trận khóa: Sử dụng ma trận kích thước 5x5.

Xử lý ký tự đặc biệt: Bảng chữ cái tiếng Anh gồm 25 ký tự, trong đó chữ J được gộp chung với chữ I.

Tiền xử lý bản rõ (Plaintext):

Loại bỏ toàn bộ khoảng trắng và ký tự không phải chữ cái.

Chuyển đổi toàn bộ văn bản thành chữ IN HOA.

Tách văn bản thành các cặp 2 ký tự (digraphs).

Chèn ký tự giả (Padding): Chèn ký tự X nếu hai ký tự trong một cặp trùng nhau (ví dụ: EE -> EX E).

Cân bằng: Chèn ký tự X vào cuối nếu tổng số ký tự của chuỗi bị lẻ.

📁 Cấu trúc thư mục
playfair.py: File nguồn chứa toàn bộ logic thuật toán (Khởi tạo ma trận, Mã hóa, Giải mã).

README.md: Tài liệu mô tả dự án và hướng dẫn sử dụng (file này).

🚀 Ví dụ kiểm thử (Test Case)
Chương trình được thiết lập để kiểm thử dựa trên thông điệp từ ví dụ trong buổi học:

Thông điệp gốc: Gr bx olnh wr vwxgb d fubswrjudskb frxuvh (Sau khi giải mã Caesar là: DO YOU LIKE TO STUDY A CRYPTOGRAPHY COURSE)

Từ khóa (Key): CRYPTO

Bản rõ sau tiền xử lý: DO YO UL IK ET OS TU DY AC RY PT OG RA PH YC OU RS EX

Kết quả đầu ra dự kiến:

Hiển thị ma trận 5x5 được sinh ra từ khóa CRYPTO.

Quá trình mã hóa (Encryption) tạo ra chuỗi Ciphertext tương ứng.

Quá trình giải mã (Decryption) phục hồi lại văn bản gốc và kiểm tra tính chính xác (Hiển thị PASS nếu kết quả khớp).
