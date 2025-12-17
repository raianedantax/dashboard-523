"""
Django settings for dashboard project.
... (comentários iniciais)
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# ... (outras configurações)

SECRET_KEY = 'django-insecure-=%p6mm8c6jkvib3yid83kop@8*3eeotk8_vqj$%+s6ce=r)@0u'
DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # ADICIONADO: Diz ao Django para procurar templates na pasta "templates" na raiz do projeto.
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dashboard.wsgi.application'

# Database
# ... (configuração da base de dados)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dashboard',
        'USER': 'aluno',
        'PASSWORD': 'Aluno@5184',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

# Password validation
# ... (validadores de senha)

AUTH_PASSWORD_VALIDATORS = [
    # ...
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

# ALTERADO: Ajustado para Português do Brasil
LANGUAGE_CODE = 'pt-br'

# ALTERADO: Ajustado para o fuso horário de São Paulo
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# ...

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações para arquivos de mídia (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = '/dashboard/' # Para onde ir após o login
LOGOUT_REDIRECT_URL = '/dashboard/accounts/login/' # Para onde ir após o logout
LOGIN_URL = '/dashboard/accounts/login/'
