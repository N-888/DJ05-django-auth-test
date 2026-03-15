# Django Auth Test

Учебный проект на Django с кастомной моделью пользователя, регистрацией, входом, CSRF-защитой, группами, разрешениями и адаптивным интерфейсом на Bootstrap без CDN.

## Основные возможности

- кастомная модель пользователя `CustomUser`
- уникальный `email`
- дополнительное поле `phone_number`
- удобная регистрация и вход
- автоматический вход после регистрации
- защищенный профиль
- работа с группами и разрешениями
- отдельная страница списка пользователей по permission
- CSRF-защита всех форм
- локальный Bootstrap в `static/` без CDN
- подсветка активного пункта меню
- современный адаптивный интерфейс

## Стек

- Python
- Django
- Bootstrap 5
- SQLite

## Запуск проекта

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver