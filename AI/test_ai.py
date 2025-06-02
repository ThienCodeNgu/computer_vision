from flask import Flask
import cv2
import numpy as np
import tensorflow as tf

# Tạo Flask server
app = Flask(__name__)

# Load mô hình AI
model = tf.keras.models.load_model('color_classifier_model.h5')
class_labels = ['orange', 'blue', 'red']

# Hàm chụp ảnh và dự đoán
def capture_and_predict(): 
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return "error"

    img = cv2.resize(frame, (64, 64))
    img = img.astype('float32') / 255.0
    img_input = np.expand_dims(img, axis=0)

    pred = model.predict(img_input)
    predicted_class = np.argmax(pred)
    label = class_labels[predicted_class]
    print("Dự đoán:", label)
    return label

# API nhận yêu cầu dự đoán
@app.route('/predict', methods=['GET'])
def handle_predict():
    result = capture_and_predict()
    return result

# Chạy server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
