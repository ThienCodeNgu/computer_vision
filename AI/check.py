import requests

url = "http://192.168.94.96/result"  # IP của ESP32
data = {"label": "red"}  # Hoặc nội dung bạn muốn gửi

try:
    response = requests.post(url, json=data, timeout=5)
    print("ESP32 trả lời:", response.text)
except requests.exceptions.RequestException as e:
    print("Lỗi khi gửi:", e)
