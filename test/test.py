import cv2

# Mở webcam (0 là webcam mặc định, nếu không được thì thử 1, 2...)
cap = cv2.VideoCapture(0)

# Kiểm tra webcam có mở được không
if not cap.isOpened():
    print("Không thể mở webcam")
    exit()

while True:
    # Đọc frame từ webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Không đọc được khung hình")
        break

    # Hiển thị khung hình
    cv2.imshow('Webcam Video', frame)

    # Bấm phím 'q' để thoát vòng lặp
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
