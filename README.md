# 🎬 Tool Lấy Phụ Đề Video bằng AI  #BY: Nguyễn Văn Anh

Công cụ này giúp bạn **tự động tạo và dịch phụ đề cho video** sang nhiều ngôn ngữ bằng AI, sử dụng mô hình Whisper của OpenAI.

---

## 🚀 Hướng dẫn sử dụng

### 1. Mở Terminal trong Visual Studio Code

### 2. Tải mã nguồn từ GitHub:
git clone https://github.com/Nguyen-Anh1905/ToolLayPhuDeVideo.git
cd ToolLayPhuDeVideo

### 3. Tạo môi trường ảo:
python -m venv venv

### 4. Kích hoạt môi trường ảo (Windows):
.\venv\Scripts\activate

### 5. Cài đặt thư viện cần thiết:
pip install -r requirements.txt

---

## 🧰 Cài đặt FFmpeg

1. Tải FFmpeg tại: https://www.gyan.dev/ffmpeg/builds/
2. Giải nén thư mục, ví dụ: C:\ffmpeg
3. Thêm đường dẫn C:\ffmpeg\bin vào biến môi trường Path (System Environment Variables)

---

## ✅ Chạy công cụ

Sau khi đã cài đặt đầy đủ, chạy file chính:
python main.py

---

## 📂 Đầu ra

Công cụ sẽ xuất file .srt (phụ đề) vào thư mục bạn chọn.

---

## 📌 Yêu cầu

- Python 3.8 trở lên
- Internet để tải mô hình Whisper
- Máy có GPU (nếu muốn dùng CUDA để tăng tốc – tùy chọn)

---

## 💡 Gợi ý

Bạn có thể thay đổi mô hình Whisper đang dùng (tiny, base, small, medium, large) trong mã nguồn tùy theo độ chính xác và tốc độ mong muốn.

---

📬 Liên hệ / đóng góp: https://github.com/Nguyen-Anh1905/ToolLayPhuDeVideo
