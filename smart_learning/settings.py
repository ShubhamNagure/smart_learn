"""
Django settings for smart_learning project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY'),

ALLOWED_HOSTS = ['smart-learn.onrender.com', '127.0.0.1', 'localhost']
CORS_ORIGIN_ALLOW_ALL = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

     # local apps
    'user_service.apps.UserServiceConfig',
    'course_service.apps.CourseServiceConfig',
    'enrollment_service.apps.EnrollmentServiceConfig',

    # Third party apps
    'corsheaders',
    'drf_yasg',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_rest_passwordreset',
    'phonenumber_field',
    'django_filters',
    # 'debug_toolbar',
]

# Celery settings
CELERY_BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"

AUTH_USER_MODEL = 'user_service.User'

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (       
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# INTERNAL_IPS = [
#     "127.0.0.1",
# ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@smartlearn'

ROOT_URLCONF = 'smart_learning.urls'

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

WSGI_APPLICATION = 'smart_learning.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
<<<<<<< HEAD
    # Development
=======
    #Development
>>>>>>> d4b4de0f58f466b83231e4b431f67e91528cf0ad
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': os.getenv('DB_NAME'),

        'USER': os.getenv('DB_USER'),

        'PASSWORD': os.getenv('DB_PASSWORD'),

        'HOST': os.getenv('DB_HOST'),

        'PORT': os.getenv('DB_PORT'),
<<<<<<< HEAD
    }

    
 #PRODUCTION
#     'default': dj_database_url.config(
#         default=os.getenv('DATABASE_URL'), 
#         conn_max_age=600    
#         )
=======
    },

    
 #PRODUCTION
    # 'default': dj_database_url.config(
    #     default=os.getenv('DATABASE_URL'), 
    #     conn_max_age=600    
    #     )
>>>>>>> d4b4de0f58f466b83231e4b431f67e91528cf0ad
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Time in hours about how long the token is active
DJANGO_REST_MULTITOKENAUTH_RESET_TOKEN_EXPIRY_TIME = 6

# Return 200 even if the user doesn't exist in the database
DJANGO_REST_PASSWORDRESET_NO_INFORMATION_LEAKAGE = True

# Allow password reset for a user that does not have a usable password
DJANGO_REST_MULTITOKENAUTH_REQUIRE_USABLE_PASSWORD = True


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'UPDATE_LAST_LOGIN': True,
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "name": "Authorization",
            "type": "apiKey",
            "in": "header",
        }
    },
    "USE_SESSION_AUTH": False,
}

STRIPE_SECRET = os.getenv('STRIPE_SECRET')

# Twilio Account SID and Auth Token

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')

TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

# Twilio phone number used for sending SMS messages

TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
