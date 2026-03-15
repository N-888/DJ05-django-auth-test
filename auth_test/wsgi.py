# Импортируем модуль os, чтобы настроить переменную окружения с настройками проекта.
import os
# Импортируем функцию создания WSGI-приложения.
from django.core.wsgi import get_wsgi_application


# Указываем Django путь к файлу настроек проекта.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_test.settings")

# Создаем WSGI-приложение проекта.
application = get_wsgi_application()