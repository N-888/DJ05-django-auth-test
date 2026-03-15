#!/usr/bin/env python
# Импортируем модуль os, чтобы работать с переменными окружения.
import os
# Импортируем модуль sys, чтобы передавать аргументы командной строки.
import sys


# Создаем основную функцию запуска административных команд Django.
def main():
    # Сообщаем Django, какой файл настроек использовать по умолчанию.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_test.settings")
    # Пытаемся импортировать стандартную функцию запуска команд Django.
    try:
        # Импортируем функцию, которая выполняет команды вроде runserver и migrate.
        from django.core.management import execute_from_command_line
    # Ловим ошибку, если Django не установлен.
    except ImportError as exc:
        # Выбрасываем более понятную ошибку с подсказкой про виртуальное окружение.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? "
            "Did you forget to activate a virtual environment?"
        ) from exc
    # Запускаем переданную в терминале команду Django.
    execute_from_command_line(sys.argv)


# Проверяем, что файл запущен напрямую.
if __name__ == "__main__":
    # Вызываем функцию main.
    main()