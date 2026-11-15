# Kitob do'koni (bookstore_app)

## Modellar
- Category: janr nomi
- Author: muallif (name, bio)
- Book: title, author, price, category, writer, image, file
- Order: user, book, quantity, status, created_at

## Sahifalar
- /bookstore/books/ : kitoblar ro'yxati
- /bookstore/books/<id>/ : kitob tafsiloti
- /bookstore/books/add/ : kitob qo'shish formasi
- /bookstore/books/<id>/edit/ : kitobni tahrirlash
- /bookstore/books/<id>/delete/ : kitobni o'chirish
- /bookstore/orders/add/ : buyurtma berish
- /bookstore/orders/ : mening buyurtmalarim
- /bookstore/register/, /login/, /logout/ : autentifikatsiya
- /api/bookstore/ : REST API

## Foydalanuvchi rollari
- Mehmon: faqat login/register sahifalarini ko'radi
- Foydalanuvchi: kitoblarni ko'radi, buyurtma beradi
- Admin: admin paneldan kitob, muallif va buyurtmalarni boshqaradi