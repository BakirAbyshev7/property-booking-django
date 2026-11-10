# Property Booking — веб-система онлайн-бронирования недвижимости

Проект производственной практики (КГТУ им. И. Раззакова, «Программная инженерия»).
Django + Django REST Framework + PostgreSQL.

## Возможности
- Регистрация и авторизация пользователей (`users`)
- Каталог объектов недвижимости: апартаменты, дома, виллы (`properties`)
- Бронирование объектов (`bookings`)
- Отзывы (`reviews`)

## Запуск
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export DB_PASSWORD=your_password   # PostgreSQL, БД real_estate_db
python manage.py migrate
python manage.py runserver
```
