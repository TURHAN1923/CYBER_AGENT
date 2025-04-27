import requests

# API URL'yi tanımlayın
IO_NET_API_URL = "https://api.intelligence.io.solutions/api/v1"  # Gerçek API URL'sini buraya girin

def ask_io_net(prompt, model="meta-llama/Llama-3.3-70B-Instruct"):
    # API URL'sini doğru şekilde kullan
    url = IO_NET_API_URL

    # API Anahtarınızı buraya ekleyin
    api_key = "io-v2-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJvd25lciI6Ijg0ZGYyNDM1LWZlZWUtNDE4NC04MzBjLTU3NzkyMzM5MWIyMSIsImV4cCI6NDg5OTM4MjQ4Mn0.dx5qP9ZHER8kS_iJYLH0CULQ5r64_rJi01yub7cG8KVDANRLtGwHNEi7xEAPLXrjV-FZN8HMucvFoMwHzlWTcg"  # API anahtarınızı buraya ekleyin

    headers = {
        "Authorization": f"Bearer {api_key}",  # API anahtarınızı 'Bearer' olarak ekliyoruz
        "Content-Type": "application/json"
    }

    data = {"prompt": prompt, "model": model}

    # API'ye POST isteği gönder
    response = requests.post(url, json=data, headers=headers)

    # JSON yanıtını döndür
    return response.json()
