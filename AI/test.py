import cv2
import os

# === CẤU HÌNH ===
video_path = 'E:/screen video/video5.mp4'
output1 = "video_part1.mp4"
output2 = "video_part2.mp4"

# Mở video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Không mở được video.")
    exit()

# Lấy thông tin video
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"Video có {total_frames} frames, {fps} FPS, kích thước: {width}x{height}")

# Tính điểm chia giữa video
mid_frame = total_frames // 2

# Định dạng codec và khởi tạo writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out1 = cv2.VideoWriter(output1, fourcc, fps, (width, height))
out2 = cv2.VideoWriter(output2, fourcc, fps, (width, height))

# Kiểm tra writer hoạt động
if not out1.isOpened() or not out2.isOpened():
    print("❌ Không thể tạo file video đầu ra.")
    cap.release()
    exit()

# Bắt đầu đọc và ghi video
frame_idx = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_idx < mid_frame:
        out1.write(frame)
    else:
        out2.write(frame)

    frame_idx += 1

# Giải phóng tài nguyên
cap.release()
out1.release()
out2.release()

print("✅ Đã cắt video thành 2 phần:")
print(f" - Phần 1: {output1}")
print(f" - Phần 2: {output2}")
