# نرم‌افزار حراست پارس دکل گستر

MVP فارسی و راست‌به‌چپ برای ثبت تردد، گشت QR، وقایع و تحویل شیفت. رابط واکنش‌گرا است و برای قراردادن در Android WebView آماده است.

## قابلیت‌ها

- نقش‌های مدیر حراست و نگهبان
- ورود و خروج افراد و خودروها
- ایستگاه گشت، مأموریت زمان‌دار، اسکن QR، عکس دوربین و زمان سرور
- ثبت واقعه با عکس، تحویل و تأیید شیفت، داشبورد و گزارش روزانه
- SQLite برای توسعه و PostgreSQL برای استقرار

## اجرای قدم‌به‌قدم

1. Python 3.11 یا بالاتر نصب کنید.
2. در این پوشه اجرا کنید: `python -m pip install -r requirements.txt`
3. دیتابیس را بسازید: `python manage.py migrate`
4. مدیر اولیه بسازید: `python manage.py createsuperuser`
5. سرور را اجرا کنید: `python manage.py runserver`
6. به `http://127.0.0.1:8000/admin/` بروید؛ کاربر نگهبان، ایستگاه و مأموریت بسازید. نقش مدیر از بخش Profile انتخاب می‌شود. آدرس اسکن ایستگاه‌ها در `/patrol/checkpoints/` قرار دارد و می‌تواند QR و چاپ شود.

## PostgreSQL

برای محیط اصلی متغیرهای `DB_ENGINE=postgres`، `POSTGRES_DB`، `POSTGRES_USER`، `POSTGRES_PASSWORD`، `POSTGRES_HOST` و `POSTGRES_PORT` را تنظیم و migrate را اجرا کنید. همچنین `SECRET_KEY`، `DEBUG=0` و `ALLOWED_HOSTS` را حتماً تنظیم کنید.

## موبایل و QR

برای دسترسی دوربین روی موبایل معمولاً HTTPS لازم است (localhost استثناست). WebView اندروید باید مجوز Camera داشته باشد. GPS در این نسخه عمداً فعال نشده است.
