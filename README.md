# Tool Tạo Phụ Đề Tự Động Từ Video

Công cụ này cho phép bạn tạo phụ đề tự động từ video bằng cách sử dụng mô hình Whisper của OpenAI. Hỗ trợ tăng tốc GPU với NVIDIA CUDA và có thể xuất phụ đề ở định dạng `.srt`.

---

## 🔧 Yêu Cầu Hệ Thống

- **Python**: Phiên bản **3.10+**
- **ffmpeg**: Dùng để xử lý và trích xuất audio từ video
- **GPU NVIDIA** *(khuyến khích)*: Để tăng tốc xử lý bằng CUDA

---

## ⚙️ Cài Đặt

### 1. Clone Dự Án
```bash
git clone https://github.com/Nguyen-Anh1905/ToolLayPhuDeVideo
cd ToolLayPhuDeVideo
```

### 2. Tạo Môi Trường Ảo
```bash
python -m venv venv
```

### 3. Kích Hoạt Môi Trường Ảo

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Cài Đặt Thư Viện Phụ Thuộc
```bash
pip install -r requirements.txt
```

---

## ▶️ Cách Sử Dụng

1. Đảm bảo môi trường ảo đã được kích hoạt.
2. Chạy chương trình:
   ```bash
   python main.py
   ```
3. Giao diện sẽ yêu cầu bạn:
   - **Chọn file video** cần tạo phụ đề.
   - **Chọn thư mục lưu file phụ đề** (.srt).
4. Đợi chương trình xử lý xong → phụ đề sẽ được lưu trong thư mục đã chọn.

---

## 📌 Lưu Ý

- Hệ thống sẽ **ưu tiên sử dụng GPU (CUDA)** nếu có, giúp tăng tốc độ xử lý. Nếu không có GPU, chương trình vẫn hoạt động bằng CPU nhưng sẽ **chậm hơn**.
- Nếu gặp lỗi `ffmpeg not found`, hãy kiểm tra:
  - Bạn đã **cài đặt ffmpeg**
  - Biến môi trường `PATH` đã chứa đường dẫn đến thư mục `ffmpeg/bin`
- Hỗ trợ các định dạng video phổ biến: `.mp4`, `.mkv`, `.mov`, `.avi`

---

---

## 🧠 Tác Giả

**Nguyễn Anh**  
📌 GitHub: [Nguyen-Anh1905](https://github.com/Nguyen-Anh1905)
