from api_handler import ask_io_net

def blue_team_defend(vulnerabilities):
    prompt = f"Blue Team ajansı gibi düşün. Aşağıdaki güvenlik açıklıklarına karşı savunma stratejilerini oluştur:\n{vulnerabilities}\n\n1. Hangi savunmalar uygulanabilir?\n2. Sistem güvenliğini nasıl artırabiliriz?"
    response = ask_io_net(prompt, model="meta-llama/Llama-3.3-70B-Instruct")  # Llama modelini kullanıyoruz
    return response
