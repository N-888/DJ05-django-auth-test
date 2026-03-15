# Импортируем административную панель Django.
from django.contrib import admin
# Импортируем path и include для подключения маршрутов.
from django.urls import include, path


# Создаем список основных маршрутов проекта.
urlpatterns = [
    # Подключаем админку Django.
    path("admin/", admin.site.urls),
    # Подключаем маршруты приложения main от корня сайта.
    path("", include("main.urls")),
]


# Подключаем свой обработчик ошибки 403.
handler403 = "main.views.custom_permission_denied_view"