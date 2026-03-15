# Импортируем Path, чтобы удобно собирать пути к папкам и файлам проекта.
from pathlib import Path


# Сохраняем путь к корневой папке проекта.
BASE_DIR = Path(__file__).resolve().parent.parent


# Указываем секретный ключ проекта.
# Для учебного проекта такой вариант допустим.
# Для реального проекта ключ нужно хранить безопасно, а не прямо в коде.
SECRET_KEY = "django-insecure-change-this-key-before-production"

# Включаем режим отладки для локальной разработки.
DEBUG = True

# Разрешаем локальные адреса для разработки.
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]


# Подключаем приложения Django и наше приложение main.
INSTALLED_APPS = [
    # Подключаем административную панель Django.
    "django.contrib.admin",
    # Подключаем систему аутентификации и пользователей.
    "django.contrib.auth",
    # Подключаем типы контента Django.
    "django.contrib.contenttypes",
    # Подключаем поддержку сессий.
    "django.contrib.sessions",
    # Подключаем сообщения Django.
    "django.contrib.messages",
    # Подключаем работу со статическими файлами.
    "django.contrib.staticfiles",
    # Подключаем наше основное приложение.
    "main",
]


# Подключаем middleware по порядку обработки запросов.
MIDDLEWARE = [
    # Включаем базовые механизмы безопасности Django.
    "django.middleware.security.SecurityMiddleware",
    # Подключаем поддержку сессий.
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Подключаем стандартную обработку общих HTTP-моментов.
    "django.middleware.common.CommonMiddleware",
    # Подключаем защиту от CSRF-атак.
    "django.middleware.csrf.CsrfViewMiddleware",
    # Подключаем аутентификацию пользователя в request.user.
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Подключаем систему сообщений.
    "django.contrib.messages.middleware.MessageMiddleware",
    # Подключаем защиту от clickjacking.
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# Указываем корневой файл маршрутов проекта.
ROOT_URLCONF = "auth_test.urls"


# Настраиваем шаблоны проекта.
TEMPLATES = [
    {
        # Используем стандартный шаблонизатор Django.
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Говорим Django искать шаблоны в общей папке templates.
        "DIRS": [BASE_DIR / "templates"],
        # Разрешаем искать шаблоны внутри приложений.
        "APP_DIRS": True,
        # Подключаем контекстные процессоры.
        "OPTIONS": {
            "context_processors": [
                # Добавляем отладочную информацию.
                "django.template.context_processors.debug",
                # Добавляем объект request в шаблоны.
                "django.template.context_processors.request",
                # Добавляем user и perms в шаблоны.
                "django.contrib.auth.context_processors.auth",
                # Добавляем messages в шаблоны.
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Указываем путь к WSGI-приложению.
WSGI_APPLICATION = "auth_test.wsgi.application"


# Настраиваем базу данных SQLite.
DATABASES = {
    "default": {
        # Указываем движок SQLite.
        "ENGINE": "django.db.backends.sqlite3",
        # Указываем путь к файлу базы данных.
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Подключаем валидаторы паролей Django.
AUTH_PASSWORD_VALIDATORS = [
    {
        # Проверяем схожесть пароля с данными пользователя.
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        # Проверяем минимальную длину пароля.
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        # Проверяем, не является ли пароль слишком распространенным.
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        # Проверяем, не состоит ли пароль только из цифр.
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Устанавливаем русский язык интерфейса.
LANGUAGE_CODE = "ru"

# Устанавливаем часовой пояс проекта.
TIME_ZONE = "Europe/Moscow"

# Включаем интернационализацию.
USE_I18N = True

# Включаем поддержку часовых поясов.
USE_TZ = True


# Указываем базовый URL для статических файлов.
STATIC_URL = "static/"

# Указываем дополнительные папки со статическими файлами.
STATICFILES_DIRS = [BASE_DIR / "static"]

# Указываем папку для collectstatic, если она понадобится позже.
STATIC_ROOT = BASE_DIR / "staticfiles"


# Указываем кастомную модель пользователя.
# Это нужно сделать до первых миграций проекта.
AUTH_USER_MODEL = "main.CustomUser"

# Указываем маршрут входа для редиректов неавторизованных пользователей.
LOGIN_URL = "login"

# Указываем страницу, куда пользователь попадет после успешного входа.
LOGIN_REDIRECT_URL = "profile"

# Указываем страницу, куда пользователь попадет после выхода из аккаунта.
LOGOUT_REDIRECT_URL = "index"


# Указываем тип автоматического первичного ключа для моделей.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"