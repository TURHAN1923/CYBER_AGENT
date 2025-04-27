import requests

def red_team_attack(system_info):
    url = "http://127.0.0.1:5000/red_attack"
    headers = {"Content-Type": "application/json"}
    data = {"system_info": system_info}
    response = requests.post(url, json=data, headers=headers)

    # Sunucudan gelen yanıtı kontrol et
    print("Red Team Yanıtı:")
    try:
        response_data = response.json()  # JSON'a çevir
        print(response_data)  # JSON verisini yazdır
        return response_data  # JSON verisini döndür
    except Exception as e:
        print(f"Red Team yanıtında JSON hatası: {e}")
        print("Sunucudan gelen ham yanıt:")
        print(response.text)  # JSON değilse, ham metni yazdır
        return {}

def blue_team_defend(system_info):
    url = "http://127.0.0.1:5000/blue_defend"
    headers = {"Content-Type": "application/json"}
    data = {"system_info": system_info}
    response = requests.post(url, json=data, headers=headers)

    # Sunucudan gelen yanıtı kontrol et
    print("Blue Team Yanıtı:")
    try:
        response_data = response.json()  # JSON'a çevir
        print(response_data)  # JSON verisini yazdır
        return response_data  # JSON verisini döndür
    except Exception as e:
        print(f"Blue Team yanıtında JSON hatası: {e}")
        print("Sunucudan gelen ham yanıt:")
        print(response.text)  # JSON değilse, ham metni yazdır
        return {}

def calculate_risk(system_info):
    system_info = system_info.lower()

    high_risk_keywords = ["sql", "injection", "brute force", "xss", "open port", "port açık", "ftp", "ssh"]
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

def suggest_security_products(risk_level):
    if risk_level == "High Risk":
        return [
            "- Fortinet Güvenlik Duvarı (Firewall)",
            "- Cloudflare WAF (Web Application Firewall)",
            "- Rapid7 InsightVM (Vulnerability Management)",
            "- CrowdStrike Falcon (Endpoint Protection)",
            "- IBM QRadar (SIEM)"
        ]
    elif risk_level == "Medium Risk":
        return [
            "- Bitdefender GravityZone (Gelişmiş Antivirüs)",
            "- Let's Encrypt SSL Sertifikası",
            "- Nessus Home (Zafiyet Tarayıcı)"
        ]
    else:
        return [
            "- Windows Defender",
            "- Güncel Yazılım Yama Yönetimi",
            "- Temel Firewall Ayarları"
        ]

def find_related_cves(system_info):
    cve_database = {
        "apache": ("CVE-2021-41773", "Apache HTTP Server Path Traversal Açığı"),
        "ssh": ("CVE-2018-15473", "SSH Username Enumeration Vulnerability"),
        "ftp": ("CVE-2015-3306", "ProFTPD Mod_copy Komut İstismar Açığı"),
        "sql": ("CVE-2012-2122", "MySQL Authentication Bypass Vulnerability"),
        "xss": ("CVE-2019-11043", "PHP-FPM üzerinden Remote Code Execution"),
        "open port": ("-", "Açık portlar spesifik CVE içermez, genel risk oluşturur.")
    }

    system_info = system_info.lower()
    found_cves = []

    for keyword, (cve_id, description) in cve_database.items():
        if keyword in system_info:
            found_cves.append((cve_id, description))

    return found_cves

def generate_summary(risk_level):
    if risk_level == "High Risk":
        return "⚠️ Sisteminiz yüksek risk altındadır! Acil güvenlik önlemleri alınması önerilir."
    elif risk_level == "Medium Risk":
        return "ℹ️ Sisteminiz orta risk seviyesindedir. Güvenlik iyileştirmeleri yapılmalıdır."
    else:
        return "✅ Sisteminiz düşük risk seviyesindedir. Mevcut güvenlik önlemlerini sürdürmelisiniz."

def save_html_report(system_info, risk_label, actions, products, cves, red_result, blue_result, summary):
    with open("rapor.html", "w", encoding="utf-8") as file:
        file.write("<html><head><title>Güvenlik Analiz Raporu</title></head><body>")
        file.write("<h1>Güvenlik Analiz Raporu</h1>")

        file.write(f"<h2>Sistem Bilgisi</h2><p>{system_info}</p>")
        file.write(f"<h2>Risk Seviyesi</h2><p>{risk_label}</p>")

        file.write("<h2>🚨 Önerilen Acil Eylemler</h2><ul>")
        for action in actions:
            file.write(f"<li>{action}</li>")
        file.write("</ul>")

        file.write("<h2>🔐 Önerilen Güvenlik Ürünleri</h2><ul>")
        for product in products:
            file.write(f"<li>{product}</li>")
        file.write("</ul>")

        file.write("<h2>🛡️ İlgili CVE Açıkları</h2><ul>")
        if cves:
            for cve_id, desc in cves:
                file.write(f"<li>{cve_id}: {desc}</li>")
        else:
            file.write("<li>İlgili CVE bulunamadı.</li>")
        file.write("</ul>")

        file.write("<h2>🔴 Red Team Sonucu</h2>")
        file.write(f"<p>{red_result['red_team_result']}</p>")

        file.write("<h2>🔵 Blue Team Sonucu</h2>")
        file.write(f"<p>{blue_result['blue_team_result']}</p>")

        file.write("<h2>📝 Özet Değerlendirme</h2>")
        file.write(f"<p>{summary}</p>")

        file.write("</body></html>")

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

    # Güvenlik Ürünleri Önerisi
    products = suggest_security_products(risk_label)
    print("\n🔐 [Önerilen Güvenlik Ürünleri]:")
    for product in products:
        print(product)

    # CVE Bilgileri
    cves = find_related_cves(system_info)
    if cves:
        print("\n🛡️ [İlgili CVE Açıkları]:")
        for cve_id, desc in cves:
            print(f"- {cve_id}: {desc}")
    else:
        print("\n🛡️ [İlgili CVE bulunamadı.]")

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

    # Özet Mesaj
    summary = generate_summary(risk_label)
    print("\n📝 [Özet Değerlendirme]:")
    print(summary)

    # 📄 Raporu dosyaya kaydet
    with open("rapor.txt", "w", encoding="utf-8") as file:
        file.write("=== Güvenlik Analiz Raporu ===\n\n")
        file.write(f"Sistem Bilgisi: {system_info}\n")
        file.write(f"Risk Seviyesi: {risk_label}\n\n")

        file.write("🚨 Önerilen Acil Eylemler:\n")
        for action in actions:
            file.write(f"{action}\n")
        file.write("\n")

        file.write("🔐 Önerilen Güvenlik Ürünleri:\n")
        for product in products:
            file.write(f"{product}\n")
        file.write("\n")

        file.write("🛡️ İlgili CVE Açıkları:\n")
        if cves:
            for cve_id, desc in cves:
                file.write(f"- {cve_id}: {desc}\n")
        else:
            file.write("- İlgili CVE bulunamadı.\n")
        file.write("\n")

        file.write("🔴 Red Team Sonucu:\n")
        file.write(f"{red_result['red_team_result']}\n\n")

        file.write("🔵 Blue Team Sonucu:\n")
        file.write(f"{blue_result['blue_team_result']}\n\n")

        file.write("📝 Özet Değerlendirme:\n")
        file.write(f"{summary}\n\n")

        file.write("✅ Analiz tamamlandı.\n")

    print("\n📄 Rapor başarıyla 'rapor.txt' dosyasına kaydedildi!")

    # Ayrıca HTML raporunu da kaydet
    save_html_report(system_info, risk_label, actions, products, cves, red_result, blue_result, summary)
    print("\n🌐 HTML rapor başarıyla 'rapor.html' dosyasına kaydedildi!")
