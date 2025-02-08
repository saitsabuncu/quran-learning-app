# 📖 Quran Learning App 🚀  

Bu proje, **Kur’an öğrenimini kolaylaştıran bir web uygulamasıdır.**  
**Django Rest Framework** ile geliştirilen bir **backend API** içerir.  

## 📌 Özellikler  
✅ **Kullanıcı Yetkilendirme (JWT Authentication)**  
✅ **Kullanıcı Profili & Yetkilendirme Sistemi**  
✅ **Admin Panelinden Sure Yönetimi**  
✅ **API ile Sure Verilerini Çekme**  
✅ **Arapça Metin, Türkçe Meal ve Okunuş Bilgisi İçeren Sure Modeli**  
✅ **RESTful API ile JSON Formatında Veri Sağlama**  

## 📌 Kurulum  

### **1. Projeyi Klonla**  
```bash
git clone https://github.com/saitsabuncu/quran-learning-app.git
cd quran-learning-app/backend
2. Sanal Ortamı Oluştur ve Aktifleştir
```bash
python -m venv ql
source ql/bin/activate  # Mac/Linux
ql\Scripts\activate  # Windows
3. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
4. Veritabanını Güncelle ve Admin Kullanıcısı Oluştur
```bash
python manage.py migrate
python manage.py createsuperuser
5. Sunucuyu Çalıştır
```bash
python manage.py runserver
📌 API Kullanımı
1. Kullanıcı Kayıt Olma
```bash
POST http://127.0.0.1:8000/api/register/
2. Kullanıcı Giriş Yapma (JWT Token Alma)
```bash
POST http://127.0.0.1:8000/api/login/
3. Kullanıcı Profili Görüntüleme (Giriş Yapmış Kullanıcılar İçin)
```bash
GET http://127.0.0.1:8000/api/profile/
4. Tüm Sureleri Çekme
```bash
GET http://127.0.0.1:8000/api/surahs/

