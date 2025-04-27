import requests

url = "http://127.0.0.1:5000/blue_defend"
headers = {"Content-Type": "application/json"}
data = {
    "vulnerabilities": "Apache server açık, SSH portu açık, SQL Injection mevcut"
}

response = requests.post(url, json=data, headers=headers)

print("\n=== Sunucudan Gelen Ham Cevap ===")
print(response.text)

try:
    print("\n=== JSON Cevap ===")
    print(response.json())
except Exception as e:
    print("\n❗ JSON formatında değil! Hata:", e)
