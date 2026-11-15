# Kitob do'koni (bookstore_app)

Django yordamida yaratilgan kitob do'koni veb-ilovasi (Introduction to Django kursi, yakuniy loyiha).

## Modellar
- Category: janr nomi
- Author: muallif (name, bio)
- Book: title, author, price, category, writer, image, file
- Order: user, book, quantity, status, created_at

## Sahifalar
- `/bookstore/books/` : kitoblar ro'yxati
- `/bookstore/books/<id>/` : kitob tafsiloti
- `/bookstore/books/add/` : kitob qo'shish formasi
- `/bookstore/books/<id>/edit/` : kitobni tahrirlash
- `/bookstore/books/<id>/delete/` : kitobni o'chirish
- `/bookstore/orders/add/` : buyurtma berish
- `/bookstore/orders/` : mening buyurtmalarim
- `/bookstore/register/`, `/bookstore/login/`, `/bookstore/logout/` : autentifikatsiya
- `/api/bookstore/` : REST API

## Foydalanuvchi rollari
- Mehmon: faqat login/register sahifalarini ko'radi
- Foydalanuvchi: kitoblarni ko'radi va buyurtma beradi
- Admin (staff): kitoblarni qo'shadi, tahrirlaydi, o'chiradi; muallif va buyurtmalarni admin paneldan boshqaradi

## Ishga tushirish
```powershell
pip install django djangorestframework Pillow pytest pytest-django
python manage.py migrate
python manage.py runserver
```

## Testlar
```powershell
python -m pytest
```