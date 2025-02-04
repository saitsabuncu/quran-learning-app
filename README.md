# quran-learning-app
```md
# Kur’an Öğrenme Uygulaması

Bu proje, Kur’an öğrenmeyi ve ezber yapmayı kolaylaştırmak için geliştirilmiş bir web ve mobil uygulamasıdır.

## 📌 Özellikler
- **Kur’an Okuma Modülü**: Sure ve ayet bazlı okuma
- **Ezber Takibi**: Kullanıcının ilerlemesini kaydetmesi
- **Tecvit Kuralları**: Renk kodlamaları ve sesli rehber
- **Sesli Okuma Desteği**: Kullanıcının telaffuz analizini yapma

## 🛠️ Kullanılan Teknolojiler
- **Frontend:** React.js / Next.js (PWA uyumlu)
- **Backend:** Django REST Framework (API)
- **Veritabanı:** PostgreSQL
- **Mobil:** React Native
- **Ses Analizi:** OpenAI Whisper API / TensorFlow

## 📌 Kurulum
Projeyi çalıştırmak için:

1. Depoyu klonla:
   ```bash
   git clone https://github.com/kullanici-adin/quran-learning-app.git
   ```
2. Backend kurulumunu yap:
   ```bash
   cd backend
   pip install -r requirements.txt
   python manage.py runserver
   ```
3. Frontend başlat:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
