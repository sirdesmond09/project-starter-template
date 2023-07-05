"""
Django settings for config project.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from django.utils.timezone import timedelta

from configurations import Configuration, values
import firebase_admin
from firebase_admin import credentials
import json



class Common(Configuration):
    
    FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
    
    cred = credentials.Certificate(json.loads(FIREBASE_CREDENTIALS))
    firebase_admin.initialize_app(cred)

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = []

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',

        'django_extensions',
        'debug_toolbar',

        'accounts.apps.AccountsConfig',
        'main.apps.MainConfig',
        "social_auth",
        
        'rest_framework',
        'djoser',
        'drf_yasg',
        'coreapi',
        'corsheaders',
        'rest_framework_simplejwt.token_blacklist',
        'storages',

    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'config.urls'

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

    WSGI_APPLICATION = 'config.wsgi.application'
    
    APPEND_SLASH=True

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )

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

    TIME_ZONE = 'Africa/Lagos'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/4.1/howto/static-files/
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
    

    # Default primary key field type
    # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    AUTH_USER_MODEL = 'accounts.User'
    
    

    DJOSER = {
        "USER_ID_FIELD" : "id",
        'LOGIN_FIELD': 'email',
        'USER_CREATE_PASSWORD_RETYPE': True,
        'USERNAME_CHANGED_EMAIL_CONFIRMATION':True,
        'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
        'SEND_ACTIVATION_EMAIL':False,
        'SEND_CONFIRMATION_EMAIL':False,
        'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
        'USERNAME_RESET_CONFIRM_URL': 'username/reset/confirm/{uid}/{token}',
        "PASSWORD_RESET_CONFIRM_RETYPE" : True,
        "SET_PASSWORD_RETYPE" : True,
        "PASSWORD_RESET_SHOW_EMAIL_NOT_FOUND":True,
        'ACTIVATION_URL' : 'activate/{uid}/{token}',
        'SERIALIZERS':{
            'user_create': 'accounts.serializers.UserRegistrationSerializer',
            'user': 'accounts.serializers.CustomUserSerializer',
            'user_delete': 'accounts.serializers.UserDeleteSerializer',
            "current_user" : 'accounts.serializers.CustomUserSerializer',
        },
        "EMAIL" : {
            'password_reset': 'accounts.emails.CustomPasswordResetEmail',  
        } 
    }


    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),


        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
        
    }

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
        'UPDATE_LAST_LOGIN': True,
        'SIGNING_KEY': SECRET_KEY,
        'AUTH_HEADER_TYPES': ('Bearer',),
        'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
        'ROTATE_REFRESH_TOKENS': True,
        'BLACKLIST_AFTER_ROTATION': True,
        

    }

    #Cors headers
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True

    SWAGGER_SETTINGS = {
        'SECURITY_DEFINITIONS': {
            'Bearer': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header'
            }
            }
        }
    
    
    AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']
    
    
    LOGIN_URL = '/admin/login/'
    SITE_NAME = ""
    DOMAIN = ""
    
    #OAuth credentials
    GOOGLE_CLIENT_ID= os.getenv("GOOGLE_CLIENT_ID")
    
    # Azure Blob Storage settings or use any storage you want
    AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
    AZURE_CONTAINER = os.getenv("AZURE_CONTAINER")
    AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
    AZURE_CONNECTION_TIMEOUT_SECS = 60


    DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage' #change to the correct storage backend from django-storages
    AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

    MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_CONTAINER}/'
    # MEDIA_ROOT = ''
    
    #use any email backend 
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = "smtp.mailgun.org"
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = 465
    EMAIL_USE_SSL = True
    EMAIL_USE_TLS = False 
    DEFAULT_FROM_EMAIL = ""
    
    
    # Configure the logging settings
    LOG_DIR = os.path.join(BASE_DIR, 'logs')

    # Ensure the logs directory exists
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Logging configuration for errors
    LOG_FILE_ERROR = os.path.join(LOG_DIR, 'error.log')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'error_file': {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': LOG_FILE_ERROR,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['error_file'],
                'level': 'ERROR',
                'propagate': True,
            },
        },
    }

    # Logging configuration for server prints
    LOG_FILE_SERVER = os.path.join(LOG_DIR, 'server.log')
    LOGGING['handlers']['server_file'] = {
        'level': 'INFO',
        'class': 'logging.FileHandler',
        'filename': LOG_FILE_SERVER,
        'formatter': 'verbose',
    }
    LOGGING['loggers']['django.server'] = {
        'handlers': ['server_file'],
        'level': 'INFO',
        'propagate': False,
    }

    # Logging formatter
    LOGGING['formatters'] = {
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    }




class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(',')

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]
    
    # DATABASES = values.DatabaseURLValue(
    #     'sqlite:///{}'.format(os.path.join(Common.BASE_DIR, 'db.sqlite3'))
    # )
    
    DATABASES = values.DatabaseURLValue(
        os.getenv("DATABASE_URL")
    )
    
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = ""


class Staging(Common):
    """
    The in-staging settings.
    """
    
    # Security
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    SECURE_REDIRECT_EXEMPT = values.ListValue([])
    SECURE_SSL_HOST = values.Value(None)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    SECURE_PROXY_SSL_HEADER = values.TupleValue(
        ('HTTP_X_FORWARDED_PROTO', 'https')
    )
    
    DEBUG = True
    DATABASES = values.DatabaseURLValue(
        os.getenv("DATABASE_URL")
    )
    

    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(',')
    CSRF_TRUSTED_ORIGINS = os.getenv("TRUSTED_ORIGINS").split(',')


class Production(Staging):
    """
    The in-production settings.
    """
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(',')
    CSRF_TRUSTED_ORIGINS = os.getenv("TRUSTED_ORIGINS").split(',')