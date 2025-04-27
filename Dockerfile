# Temel imaj
FROM python:3.10-slim

# Çalışma dizini
WORKDIR /app

# Tüm dosyaları kopyala
COPY . .

# Gereken kütüphaneleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Programı çalıştır
CMD ["python", "client_app.py"]
