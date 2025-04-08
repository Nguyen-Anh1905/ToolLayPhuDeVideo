# 
#                             Áp dụng cho xủa lí 1 video


import whisper
import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import torch

print("CUDA Available:", torch.cuda.is_available())

def convert_to_wav(video_path, wav_path):
    command = [
        "ffmpeg",
        "-i", video_path,
        "-ar", "16000",
        "-ac", "1",
        "-y", wav_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def transcribe_with_whisper(wav_path, output_srt_path):
    model = whisper.load_model("medium")  # ✅ dùng model 'medium'
    result = model.transcribe(wav_path, fp16=torch.cuda.is_available())

    with open(output_srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"], start=1):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"].strip()
            f.write(f"{i}\n")
            f.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
            f.write(f"{text}\n\n")

def format_timestamp(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    ms = int((seconds - int(seconds)) * 1000)
    return f"{hrs:02}:{mins:02}:{secs:02},{ms:03}"

def select_video():
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mkv *.mov *.avi")])
    if not video_path:
        return

    # 👉 Chọn thư mục lưu file
    output_dir = filedialog.askdirectory(title="Chọn thư mục lưu file SRT")
    if not output_dir:
        return

    base_name = os.path.splitext(os.path.basename(video_path))[0]
    wav_path = os.path.join(output_dir, base_name + ".wav")
    srt_path = os.path.join(output_dir, base_name + ".srt")

    print("🎧 Đang chuyển đổi video sang âm thanh...")
    convert_to_wav(video_path, wav_path)

    print("🧠 Đang nhận diện giọng nói bằng Whisper (medium)...")
    transcribe_with_whisper(wav_path, srt_path)

    print(f"✅ Đã tạo phụ đề tại: {srt_path}")
    
    if os.path.exists(wav_path):
        os.remove(wav_path)

# Chạy chương trình
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    select_video()
