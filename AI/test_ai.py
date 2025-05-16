import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import requests

# Load mô hình đã huấn luyện
model = tf.keras.models.load_model('color_classifier_model.h5')

# Mở webcam (0 = webcam mặc định)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không mở được webcam.")
    exit()

print("Nhấn SPACE để chụp ảnh, ESC để thoát.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Không đọc được frame.")
        break

    # Hiển thị frame lên cửa sổ
    cv2.imshow('Webcam - Nhấn SPACE để chụp', frame)

    key = cv2.waitKey(1)
    if key % 256 == 27:  # ESC
        print("Đã thoát.")
        break
    elif key % 256 == 32:  # SPACE
        # Resize ảnh và chuẩn hóa
        img_resized = cv2.resize(frame, (64, 64))
        img_normalized = img_resized.astype('float32') / 255.0
        img_input = np.expand_dims(img_normalized, axis=0)

        # Dự đoán
        pred = model.predict(img_input)
        predicted_class = np.argmax(pred)
        class_labels = ['orange', 'blue', 'red']
        label = class_labels[predicted_class]

        print("Dự đoán:", label)

        # Gửi kết quả cho ESP32
        url = "http://192.168.94.96/result"  # IP của ESP32
        try:
            response = requests.post(url, data=label, timeout=5)
            print("ESP32 trả lời:", response.text)
        except requests.exceptions.RequestException as e:
            print("Lỗi khi gửi:", e)

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
