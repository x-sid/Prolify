"""
Django settings for prolify project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6f*wr@rsdr%h)p*i*f8&bs65ef(&7ue7(treveu#8y-0kw#$+_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'album.apps.AlbumConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'prolify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'prolify.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')

MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/' 

# in settings.py
LOGIN_URL = '/accounts/login/'     # this should coinside with url pattern of login view
LOGOUT_URL = '/accounts/login/'   # same but for logout view
LOGIN_REDIRECT_URL = '/' # url to main page

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True
ACCOUNT_AUTHENTICATION_METHOD ='username_email'
ACCOUNT_CONFIRM_EMAIL_ON_GET =False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL =LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =3
ACCOUNT_EMAIL_CONFIRMATION_HMAC =True
ACCOUNT_EMAIL_REQUIRED =False
ACCOUNT_EMAIL_VERIFICATION ='optional'
ACCOUNT_EMAIL_SUBJECT_PREFIX ='[Site]'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'
ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN =180
ACCOUNT_EMAIL_MAX_LENGTH=254
ACCOUNT_FORMS ={}
ACCOUNT_LOGIN_ATTEMPTS_LIMIT =''
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT=300
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION =True
ACCOUNT_LOGOUT_ON_GET =False
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE =False
ACCOUNT_LOGIN_ON_PASSWORD_RESET =False
ACCOUNT_SIGNUP_FORM_CLASS =None
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE =True
ACCOUNT_USERNAME_BLACKLIST =[]
ACCOUNT_UNIQUE_EMAIL =True
ACCOUNT_USER_MODEL_EMAIL_FIELD ='email'
ACCOUNT_USER_MODEL_USERNAME_FIELD ='username'
ACCOUNT_USERNAME_MIN_LENGTH =5
ACCOUNT_USERNAME_REQUIRED =True


EMAIL_HOST='127.0.0.1'
EMAIL_PORT=1025
