# Импортируем модуль администратора Django.
from django.contrib import admin
# Импортируем стандартную админ-конфигурацию пользователя.
from django.contrib.auth.admin import UserAdmin

# Импортируем нашу кастомную модель пользователя.
from .models import CustomUser


# Регистрируем нашу модель в админке.
@admin.register(CustomUser)
# Создаем кастомную конфигурацию админки для пользователя.
class CustomUserAdmin(UserAdmin):
    # Указываем, какие поля будут видны в списке пользователей.
    list_display = ("username", "email", "phone_number", "is_staff", "is_active")
    # Добавляем фильтры справа.
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    # Добавляем поиск по username, email и телефону.
    search_fields = ("username", "email", "phone_number")
    # Добавляем наше поле phone_number в форму редактирования пользователя.
    fieldsets = UserAdmin.fieldsets + (
        (
            "Дополнительные поля",
            {
                "fields": ("phone_number",),
            },
        ),
    )
    # Добавляем email и phone_number в форму создания пользователя в админке.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Дополнительные поля",
            {
                "fields": ("email", "phone_number"),
            },
        ),
    )