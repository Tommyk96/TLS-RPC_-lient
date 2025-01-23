import os
from pathlib import Path
from .tls_config import CERTIFICATE, PRIVATE_KEY
from django.core.management.utils import get_random_secret_key

# Генерация случайного секретного ключа для вашего проекта
# Рекомендуется генерировать новый ключ при каждом разворачивании
print(get_random_secret_key())

# BASE_DIR должен быть определен с использованием pathlib.Path
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', '[::1]', 'ssldomain.com']

ROOT_URLCONF = 'jsonrpc_client.urls'

# Убедитесь, что папка static существует
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Эта папка должна существовать
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Убедитесь, что папка templates существует и содержит ваши шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Путь к папке шаблонов
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions', 
    # Другие приложения...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

# Настройки для статичных файлов
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Убедитесь, что эта папка существует
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Настройки для медиа-файлов
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'admin_user',
        'PASSWORD': 'Brouser77',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Настройки безопасности
SECURE_SSL_REDIRECT = True  # Для локальной разработки можно оставить False
SECURE_HSTS_SECONDS = 31536000 # Для локальной разработки оставляем 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_SECURE = True  # Для локальной разработки оставляем False
CSRF_COOKIE_SECURE = True  # Для локальной разработки оставляем False
DEBUG = True

# Настройки сессий и кеширования
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_AGE = 3600
CACHE_BACKEND = 'django.core.cache.backends.locmem.LocMemCache'

# Секретный ключ
SECRET_KEY = get_random_secret_key()  # Лучше использовать сгенерированный ключ

# Путь к SSL сертификатам
SSL_CERTIFICATE_PATH = "/home/fantomas/client-tool/jsonrpc_client/certificate.pem"
SSL_PRIVATE_KEY_PATH = "/home/fantomas/client-tool/jsonrpc_client/private_key.pem"

