# Импортируем AbstractUser, чтобы расширить стандартную модель пользователя Django.
from django.contrib.auth.models import AbstractUser
# Импортируем модели Django.
from django.db import models


# Создаем кастомную модель пользователя на основе стандартного AbstractUser.
class CustomUser(AbstractUser):
    # Переопределяем поле email, чтобы сделать его обязательным и уникальным.
    email = models.EmailField(
        # Задаем человекочитаемое имя поля.
        verbose_name="Электронная почта",
        # Делаем поле уникальным.
        unique=True,
    )

    # Добавляем поле номера телефона.
    phone_number = models.CharField(
        # Задаем человекочитаемое имя поля.
        verbose_name="Номер телефона",
        # Ограничиваем максимальную длину строки.
        max_length=20,
        # Разрешаем не заполнять поле в формах.
        blank=True,
        # Разрешаем хранить NULL в базе данных.
        null=True,
        # Делаем поле уникальным, если значение указано.
        unique=True,
    )

    # Описываем дополнительную метаинформацию модели.
    class Meta(AbstractUser.Meta):
        # Задаем имя модели в единственном числе.
        verbose_name = "Пользователь"
        # Задаем имя модели во множественном числе.
        verbose_name_plural = "Пользователи"
        # Добавляем собственное permission для страницы списка пользователей.
        permissions = [
            ("view_user_directory", "Может просматривать список пользователей"),
        ]

    # Определяем строковое представление пользователя.
    def __str__(self):
        # Возвращаем username, чтобы пользователь красиво отображался в админке и консоли.
        return self.username