from api_handler import ask_io_net

def red_team_attack(system_info):
    prompt = f"Red Team ajansı gibi düşün. Sistemdeki potansiyel güvenlik açıklarını bulmaya çalış.\nSistem Bilgisi: {system_info}\n\n1. Hangi saldırılar uygulanabilir?\n2. Hangi araçlar ve yöntemler kullanılabilir?\n3. Saldırı planını detaylıca belirt."
    response = ask_io_net(prompt, model="meta-llama/Llama-3.3-70B-Instruct")  # Llama modelini kullanıyoruz
    return response
