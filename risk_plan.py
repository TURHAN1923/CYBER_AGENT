import requests

def red_team_attack(system_info):
    url = "http://127.0.0.1:5000/red_attack"
    headers = {"Content-Type": "application/json"}
    data = {"system_info": system_info}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def blue_team_defend(vulnerabilities):
    url = "http://127.0.0.1:5000/blue_defend"
    headers = {"Content-Type": "application/json"}
    data = {"vulnerabilities": vulnerabilities}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def calculate_risk(system_info):
    system_info = system_info.lower()

    # High risk anahtar kelimeler
    high_risk_keywords = ["sql", "injection", "brute force", "xss", "open port", "port açık", "ftp", "ssh","truva"]

    # Medium risk anahtar kelimeler
    medium_risk_keywords = ["zayıf şifre", "ssl yok", "güncel değil"]

    for keyword in high_risk_keywords:
        if keyword in system_info:
            return "High Risk"

    for keyword in medium_risk_keywords:
        if keyword in system_info:
            return "Medium Risk"

    return "Low Risk"


def generate_emergency_actions(risk_level):
    if risk_level == "High Risk":
        return [
            "1. Açık portları acilen kapatın veya güvenli hale getirin.",
            "2. Şifreleme ve güvenlik protokollerini uygulayın (SSL, VPN vb.).",
            "3. Hızlı bir sızma testi (penetration test) yaptırın."
        ]
    elif risk_level == "Medium Risk":
        return [
            "1. Şifre politikalarını güçlendirin (karmaşık şifreler zorunlu olsun).",
            "2. SSL sertifikalarını kontrol edin ve eksikleri giderin.",
            "3. Sistem yamalarını ve güncellemeleri hemen uygulayın."
        ]
    else:
        return [
            "1. Mevcut güvenlik önlemlerini sürdürün.",
            "2. Periyodik güvenlik taramaları yapın.",
            "3. Çalışanlara temel siber güvenlik eğitimi verin."
        ]

if __name__ == "__main__":
    print("\n=== Red Team & Blue Team Güvenlik Analiz Aracı ===\n")

    system_info = input("Sistem bilgisi giriniz (örnek: Apache server açık, SSH portu açık): ")

    # Risk Analizi
    risk_label = calculate_risk(system_info)
    print(f"\n📊 [Risk Seviyesi]: {risk_label}\n")

    # Acil Eylemler
    actions = generate_emergency_actions(risk_label)
    print("🚨 [Önerilen Acil Eylemler]:")
    for action in actions:
        print(action)

    # Red Team Analizi
    print("\n🔴 [Red Team Analizi Başlatılıyor...]")
    red_result = red_team_attack(system_info)
    print("\n🛡️ [Red Team Sonucu]:")
    print(red_result['red_team_result'])

    # Blue Team Analizi
    print("\n🔵 [Blue Team Savunması Başlatılıyor...]")
    blue_result = blue_team_defend(system_info)
    print("\n🛡️ [Blue Team Sonucu]:")
    print(blue_result['blue_team_result'])

    print("\n✅ === Analiz Tamamlandı! Güvende kalın. ===\n")
