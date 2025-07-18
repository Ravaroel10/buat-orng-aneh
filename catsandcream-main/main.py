import requests

# Ganti dengan path gambar kamu
file_path = "your_image.png"
receiver_ip = "10.5.60.127"  # Ganti dengan IP laptop

url = f"http://10.5.60.16:9000/upload"

with open(file_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print("Status:", response.status_code)
print("Response:", response.text)
