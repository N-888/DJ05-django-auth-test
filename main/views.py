# Импортируем messages, чтобы показывать пользователю уведомления.
from django.contrib import messages
# Импортируем функцию login, чтобы автоматически авторизовать пользователя после регистрации.
from django.contrib.auth import login
# Импортируем миксины ограничения доступа.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
# Импортируем готовое представление входа Django.
from django.contrib.auth.views import LoginView
# Импортируем render для возврата HTML-страниц.
from django.shortcuts import render
# Импортируем reverse_lazy для безопасной работы с URL в классах.
from django.urls import reverse_lazy
# Импортируем стандартные generic views Django.
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView

# Импортируем наши формы.
from .forms import CustomAuthenticationForm
from .forms import CustomUserCreationForm
# Импортируем нашу модель пользователя.
from .models import CustomUser


# Создаем представление главной страницы.
class IndexView(TemplateView):
    # Указываем шаблон главной страницы.
    template_name = "index.html"


# Создаем представление страницы профиля.
class ProfileView(LoginRequiredMixin, TemplateView):
    # Указываем шаблон страницы профиля.
    template_name = "profile.html"
    # Указываем маршрут входа, если пользователь не авторизован.
    login_url = reverse_lazy("login")


# Создаем представление списка пользователей.
class UserDirectoryView(PermissionRequiredMixin, ListView):
    # Указываем модель, список которой будем выводить.
    model = CustomUser
    # Указываем шаблон страницы со списком пользователей.
    template_name = "user_directory.html"
    # Указываем имя переменной в шаблоне.
    context_object_name = "users"
    # Указываем permission, которое нужно для доступа.
    permission_required = "main.view_user_directory"
    # Говорим Django отдавать ошибку 403, а не просто редиректить.
    raise_exception = True
    # Задаем queryset с сортировкой по дате регистрации.
    queryset = CustomUser.objects.order_by("-date_joined")


# Создаем собственное представление входа.
class CustomLoginView(LoginView):
    # Указываем шаблон страницы входа.
    template_name = "login.html"
    # Подключаем нашу кастомную форму входа.
    authentication_form = CustomAuthenticationForm
    # Если пользователь уже вошел в систему, сразу перенаправляем его дальше.
    redirect_authenticated_user = True


# Создаем представление регистрации.
class RegisterView(CreateView):
    # Указываем форму регистрации.
    form_class = CustomUserCreationForm
    # Указываем шаблон страницы регистрации.
    template_name = "register.html"
    # Указываем адрес, куда перенаправить пользователя после успешной регистрации.
    success_url = reverse_lazy("profile")

    # Переопределяем успешную обработку формы.
    def form_valid(self, form):
        # Сначала выполняем стандартное сохранение пользователя.
        response = super().form_valid(form)
        # Получаем только что созданного пользователя.
        user = self.object
        # Сразу авторизуем пользователя в текущей сессии.
        login(self.request, user)
        # Показываем сообщение об успешной регистрации.
        messages.success(self.request, "Регистрация прошла успешно. Добро пожаловать!")
        # Возвращаем стандартный ответ с редиректом.
        return response


# Создаем собственный обработчик ошибки 403.
def custom_permission_denied_view(request, exception):
    # Возвращаем страницу недостатка прав со статусом 403.
    return render(request, "permission_denied.html", status=403)