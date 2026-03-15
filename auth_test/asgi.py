# Импортируем модуль os, чтобы настроить переменную окружения с настройками проекта.
import os
# Импортируем функцию создания ASGI-приложения.
from django.core.asgi import get_asgi_application


# Указываем Django путь к файлу настроек проекта.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_test.settings")

# Создаем ASGI-приложение проекта.
application = get_asgi_application()