# Импортируем модуль forms Django.
from django import forms
# Импортируем стандартную форму входа.
from django.contrib.auth.forms import AuthenticationForm
# Импортируем стандартную форму создания пользователя.
from django.contrib.auth.forms import UserCreationForm

# Импортируем нашу кастомную модель пользователя.
from .models import CustomUser


# Создаем кастомную форму регистрации на базе стандартной UserCreationForm.
class CustomUserCreationForm(UserCreationForm):
    # Создаем поле email вручную, чтобы гибко настроить его отображение.
    email = forms.EmailField(
        # Указываем подпись поля.
        label="Электронная почта",
        # Делаем поле обязательным.
        required=True,
    )

    # Создаем поле телефона вручную, чтобы гибко настроить его отображение.
    phone_number = forms.CharField(
        # Указываем подпись поля.
        label="Номер телефона",
        # Разрешаем оставить поле пустым.
        required=False,
    )

    # Описываем, с какой моделью и какими полями работает форма.
    class Meta(UserCreationForm.Meta):
        # Указываем модель формы.
        model = CustomUser
        # Перечисляем поля формы в нужном порядке.
        fields = ("username", "email", "phone_number", "password1", "password2")

    # Переопределяем инициализацию формы.
    def __init__(self, *args, **kwargs):
        # Вызываем родительскую инициализацию.
        super().__init__(*args, **kwargs)

        # Добавляем Bootstrap-классы и подсказки для поля username.
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "Например, maria",
                "autofocus": True,
            }
        )

        # Добавляем Bootstrap-классы и подсказки для поля email.
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "Например, maria@example.com",
            }
        )

        # Добавляем Bootstrap-классы и подсказки для поля phone_number.
        self.fields["phone_number"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "Например, +7 999 123-45-67",
            }
        )

        # Добавляем Bootstrap-классы и подсказки для поля password1.
        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "Придумай надежный пароль",
            }
        )

        # Добавляем Bootstrap-классы и подсказки для поля password2.
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "Повтори пароль еще раз",
            }
        )

        # Делаем пояснения к полям более понятными.
        self.fields["username"].help_text = "Разрешены буквы, цифры и символы @/./+/-/_."
        self.fields["email"].help_text = "Адрес электронной почты должен быть уникальным."
        self.fields["phone_number"].help_text = "Поле необязательное, но если заполнено, номер должен быть уникальным."
        self.fields["password1"].help_text = "Пароль должен быть надежным и не слишком простым."
        self.fields["password2"].help_text = "Введите тот же пароль еще раз для подтверждения."

    # Проверяем уникальность email.
    def clean_email(self):
        # Получаем email из очищенных данных формы.
        email = self.cleaned_data["email"]
        # Проверяем, есть ли пользователь с таким email.
        if CustomUser.objects.filter(email__iexact=email).exists():
            # Если такой email уже есть, выбрасываем ошибку валидации.
            raise forms.ValidationError("Пользователь с такой электронной почтой уже существует.")
        # Возвращаем email, если он уникален.
        return email

    # Проверяем уникальность номера телефона только если он введен.
    def clean_phone_number(self):
        # Получаем телефон из очищенных данных формы.
        phone_number = self.cleaned_data.get("phone_number")
        # Если телефон не введен, просто возвращаем пустое значение.
        if not phone_number:
            return phone_number
        # Проверяем, есть ли уже пользователь с таким номером.
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            # Если номер уже существует, выбрасываем ошибку валидации.
            raise forms.ValidationError("Пользователь с таким номером телефона уже существует.")
        # Возвращаем номер телефона, если он уникален.
        return phone_number


# Создаем кастомную форму входа, чтобы красиво стилизовать поля через Bootstrap.
class CustomAuthenticationForm(AuthenticationForm):
    # Переопределяем инициализацию формы.
    def __init__(self, request=None, *args, **kwargs):
        # Вызываем родительскую инициализацию.
        super().__init__(request=request, *args, **kwargs)

        # Стилизуем поле username.
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "Введите имя пользователя",
                "autofocus": True,
            }
        )

        # Стилизуем поле password.
        self.fields["password"].widget.attrs.update(
            {
                "class": "form-control form-control-lg",
                "placeholder": "Введите пароль",
            }
        )

        # Делаем подписи понятнее.
        self.fields["username"].label = "Имя пользователя"
        self.fields["password"].label = "Пароль"