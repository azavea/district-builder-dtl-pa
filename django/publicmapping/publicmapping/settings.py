"""
Django settings for publicmapping project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import logging.config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'foo')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['web']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 3rd party
    'django_comments',
    'django_extensions',
    'gunicorn',
    'polib',
    'rosetta',
    'tagging',

    # local
    'publicmapping',
    'redistricting',
    'reporting'
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

ROOT_URLCONF = 'publicmapping.urls'

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

WSGI_APPLICATION = 'publicmapping.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'district_builder',
        'USER': 'district_builder',
        'PASSWORD': 'district_builder',
        'HOST': 'postgres.internal.districtbuilder.com',
        'PORT': '5432'
    }
}

# Caches
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis.internal.districtbuilder.com:6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGGING_CONFIG = None
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'datefmt':
            '%Y-%m-%d %H:%M:%S %z',
            'format': ('[%(asctime)s] [%(process)d] [%(levelname)s]'
                       ' %(message)s'),
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
        },
    }
})

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'
ENABLED_LANGUAGES = ('en', 'es', 'fr', 'ja')

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/usr/src/app/static/'

# LEGACY SETTINGS

# Location of your key value store, e.g., Redis
KEY_VALUE_STORE = ''

MAP_SERVER = ''
BASE_MAPS = 'None'
MAP_SERVER_NS = 'pmp'
MAP_SERVER_NSHREF = 'https://github.com/PublicMapping/'
FEATURE_LIMIT = 100
MAP_SERVER_USER = 'GEOSERVER-ADMIN-USER'
MAP_SERVER_PASS = 'GEOSERVER-ADMIN-PASS'

ADJACENCY = False

CONVEX_CHOROPLETH = False

EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = 'None '

MEDIA_ROOT = '/usr/src/app/site-media/'

# We only use collectstatic to collect static files from installed apps
# that aren't local (eg. django.contrib.admin).
STATICFILES_FINDERS = ()

SLD_ROOT = '/opt/sld/'

WEB_TEMP = '/tmp'

CONCURRENT_SESSIONS = 5
SESSION_TIMEOUT = 15

GA_ACCOUNT = None
GA_DOMAIN = None

MAX_UPLOAD_SIZE = 5300 * 1024

FIX_UNASSIGNED_MIN_PERCENT = 99

FIX_UNASSIGNED_COMPARATOR_SUBJECT = 'poptot'

MAX_UNDOS_DURING_EDIT = 0

MAX_UNDOS_AFTER_EDIT = 0

LEADERBOARD_MAX_RANKED = 10

SITE_ID = 2

REPORTS_ENABLED = 'CALC'
