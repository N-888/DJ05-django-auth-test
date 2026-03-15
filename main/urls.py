# Импортируем стандартное представление выхода Django.
from django.contrib.auth.views import LogoutView
# Импортируем path для описания маршрутов.
from django.urls import path

# Импортируем наши представления.
from .views import CustomLoginView
from .views import IndexView
from .views import ProfileView
from .views import RegisterView
from .views import UserDirectoryView


# Создаем маршруты приложения main.
urlpatterns = [
    # Главная страница.
    path("", IndexView.as_view(), name="index"),
    # Страница входа.
    path("login/", CustomLoginView.as_view(), name="login"),
    # Страница регистрации.
    path("register/", RegisterView.as_view(), name="register"),
    # Страница профиля.
    path("profile/", ProfileView.as_view(), name="profile"),
    # Страница списка пользователей по permission.
    path("users/", UserDirectoryView.as_view(), name="user_directory"),
    # Выход из системы.
    path("logout/", LogoutView.as_view(), name="logout"),
]