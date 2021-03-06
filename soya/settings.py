"""
Django settings for soya project.

Generated by 'django-admin startproject' using Django 2.0.2.

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
SECRET_KEY = 'hv%p_=f-5(*von9h#^^!t99q=tmc_a7f-c%3+&7s051#%52%7h'

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
    'django.contrib.sites',
    'django.contrib.flatpages',
    'imagekit',
    'django.contrib.gis',
    'geo',
    'image',
    'wiki',
    'accounts',
    'jquery',
    'leaflet',
    'djgeojson',
    'bootstrap4',
    'taggit',
    'gunicorn',
    'tinymce',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'soya.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'soya.wsgi.application'

SITE_ID = 1


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
from socket import gethostname
if 'local' in gethostname():
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'soya',
            'USER': 'tam',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'soya',
            'USER': 'wakhok',
            'PASSWORD': 'wakhok+097-0013',
            'HOST': '127.0.0.1',
            'PORT': 5432,
        }
    }

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.contrib.gis.db.backends.postgis',
#        'NAME': 'soya',
#        'USER': 'wakhok',
#        'PASSWORD': 'wakhok+097-0013',
#        'HOST': 'soya-lab.jp',
#        'PORT': 5432,
#    }
#}


GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')

ALLOWED_HOSTS = ['*']

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

LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (45.109167, 141.994444),
    'CENTER': (45.109167, 141.994444),
    # 'SPATIAL_EXTENT' : (45.00, 141.0, 46.0, 142.5),
    'DEFAULT_ZOOM': 9,
    'MIN_ZOOM': 8,
    'MAX_ZOOM': 18,
    'RESET_VIEW': False,
    'CONTROL': True
}

LOGIN_REDIRECT_URL = '/' 

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

TINYMCE_JS_URL = os.path.join(BASE_DIR, "wiki/static/wiki/js/tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "wiki/static/wiki/js/tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    'theme':'advanced',
    'plugins':'table, paste, searchreplace',
    'menubar':'edit',
    'toolbar':'paste,attach',
    'theme_advanced_buttons1':'bold, paste, attach, italic, underline, bullist, numlist, link, unlink, styleselect, fontsizeselect',
    'width':'100%',
    'height':'300',
    'valid_styles':'font-weight, font-style, text-decoration',
    'fontsize_default':'24pt',
}


SERIALIZATION_MODULES = {
        "custom_geojson": "wiki.geojson_serializer",
}

FILE_UPLOAD_HANDLERS = [
'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

