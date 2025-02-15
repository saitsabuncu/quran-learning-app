# Quran Learning App

Quran Learning App, kullanıcıların Kur'an-ı Kerim'i daha etkili bir şekilde ezberlemelerine yardımcı olmak amacıyla geliştirilmiş bir web uygulamasıdır. Bu uygulama, ezberlenen sureleri ve sayfaları takip etmenize, ezberleme ilerlemenizi yönetmenize olanak tanır.

## Özellikler

- Ezberlenen surelerin ve sayfaların takibi
- Ezberleme tarihlerini görüntüleme
- Kullanıcı dostu arayüz

## Gereksinimler

- Python 3.6 veya daha üstü
- Django 5.1.5
- Diğer bağımlılıklar için `requirements.txt` dosyasını kontrol edin

## Kurulum

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/saitsabuncu/quran-learning-app.git
   cd quran-learning-app/backend
   ```

2. Sanal ortam oluşturun ve etkinleştirin:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/MacOS
   venv\Scripts\activate  # Windows
   ```

3. Gerekli paketleri yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

4. Veritabanını oluşturun ve gerekli migrasyonları uygulayın:

   ```bash
   python manage.py migrate
   ```

5. Süper kullanıcı oluşturun:

   ```bash
   python manage.py createsuperuser
   ```

6. Geliştirme sunucusunu başlatın:

   ```bash
   python manage.py runserver
   ```

Uygulama varsayılan olarak `http://127.0.0.1:8000/` adresinde çalışacaktır.

## Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Katkıda bulunmak için lütfen aşağıdaki adımları izleyin:

1. Depoyu forklayın.
2. Yeni bir dal oluşturun: `git checkout -b özellik-adi`
3. Değişikliklerinizi yapın ve commit edin: `git commit -m 'Özellik ekle: özellik açıklaması'`
4. Dalınıza push edin: `git push origin özellik-adi`
5. Bir Pull Request oluşturun.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

---
