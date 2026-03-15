# Импортируем базовый класс конфигурации приложения.
from django.apps import AppConfig


# Создаем конфигурацию приложения main.
class MainConfig(AppConfig):
    # Указываем тип автоматически создаваемого первичного ключа.
    default_auto_field = "django.db.models.BigAutoField"
    # Указываем имя приложения.
    name = "main"
    # Указываем красивое имя приложения для админки.
    verbose_name = "Основное приложение"