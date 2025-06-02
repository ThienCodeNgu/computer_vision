import cv2
import os

# === CẤU HÌNH ===
video_path = 'E:/screen video/video6.mp4'  # Đường dẫn video
output_folder = 'captured_frames'  # Thư mục lưu ảnh
capture_interval = 5               # Chụp mỗi 5 giây
start_image_index = 713        # Bắt đầu lưu từ frame_0249.jpg

# Tạo thư mục nếu chưa tồn tại
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Mở video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Không mở được video.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps * capture_interval)

frame_count = 0
image_count = start_image_index

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f"frame_{image_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Đã lưu: {filename}")
        image_count += 1

    frame_count += 1

cap.release()
print("Hoàn tất.")
