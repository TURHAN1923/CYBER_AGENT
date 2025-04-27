import requests
import json

# API URL'leri
red_url = "http://127.0.0.1:5000/red_attack"
blue_url = "http://127.0.0.1:5000/blue_defend"

# Gönderilecek bilgi
system_info = "Apache server açık, SSH portu açık."

headers = {
    "Content-Type": "application/json"
}

try:
    # Red Team İsteği
    red_response = requests.post(red_url, json={"system_info": system_info}, headers=headers)
    if red_response.status_code == 200:
        print("\n🔴 Red Team Yanıtı:")
        print(json.dumps(red_response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Red Team Hatası: {red_response.status_code}")

    # Blue Team İsteği
    blue_response = requests.post(blue_url, json={"vulnerabilities": system_info}, headers=headers)
    if blue_response.status_code == 200:
        print("\n🔵 Blue Team Yanıtı:")
        print(json.dumps(blue_response.json(), indent=4, ensure_ascii=False))
    else:
        print(f"Blue Team Hatası: {blue_response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"İstek sırasında hata oluştu: {e}")
