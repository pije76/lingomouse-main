"""
Django settings for lingomouse project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)i=66s*wr!fm992%$o=av+*i7@ili4_dy8_ft31i)%68(=c#6='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
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
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.apple',

	'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    # 'rest_framework_simplejwt',

    'frontend',
    'config',
    'course',
    'api',

	'tailwind',
	'theme',
	"crispy_forms",
	'import_export',
	# 'whoosh_index',
    'haystack',

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

ROOT_URLCONF = 'lingomouse.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'theme/templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				# 'frontend.context_processors.app_list',
			],
		},
	},
]

WSGI_APPLICATION = 'lingomouse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/uploads/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
	"127.0.0.1",
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1


#############################################################################################

# AUTH_USER_MODEL = 'two_app.CustomUser'

ACCOUNT_AUTHENTICATION_METHOD = "username"
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
ACCOUNT_SESSION_REMEMBER = None
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "optional"
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = "/accounts/logout/"
SOCIALACCOUNT_AUTO_SIGNUP=True
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = "optional"
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_STORE_TOKENS=True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '336000871218-3ra1gpbi765an9vhqo1uom9haj9bdlto.apps.googleusercontent.com',
            'secret': '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',
            'key': '',
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "offline",
        },
        # 'OAUTH_PKCE_ENABLED': True,
    },
    # "apple": {
    #     "APP": {
    #         "client_id": "your.service.id",
    #         "secret": "KEYID",
    #         "key": "MEMAPPIDPREFIX",
    #         "certificate_key": """-----BEGIN PRIVATE KEY-----
    #         s3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr
    #         3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3cr3ts3
    #         c3ts3cr3t
    #         -----END PRIVATE KEY-----
    #         """
    #     }
    # }
}


#############################################################################################

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': [
		'rest_framework.permissions.AllowAny',
	],
	'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
	'PAGE_SIZE': 5,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
}


REST_AUTH = {
    'USE_JWT': True,
#     'JWT_AUTH_COOKIE': 'my-app-auth',
#     'JWT_AUTH_REFRESH_COOKIE': 'my-refresh-token',
}

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(minutes=60),
# }


#############################################################################################

# Tailwind app setup
TAILWIND_APP_NAME = 'theme'

IMPORT_EXPORT_USE_TRANSACTIONS = True

WHOOSH_INDEX = os.path.join(BASE_DIR, 'whoosh_index/')

HAYSTACK_CONNECTIONS = {
    'default':
    {
        # 'ENGINE': 'haystack.backends.elasticsearch5_backend.Elasticsearch5SearchEngine',
        # 'URL': 'http://127.0.0.1:9200/',
        # 'INDEX_NAME': 'haystack',
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}

CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        # 'LOCATION': 'redis://127.0.0.1:6379',
        'LOCATION': '127.0.0.1:11211',
    },

}

SESSION_SAVE_EVERY_REQUEST = True

####################################################################################################


if DEBUG:
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

    MESSAGE_TAGS = {
    	messages.DEBUG: 'alert-info',
    	messages.INFO: 'alert-info',
    	messages.SUCCESS: 'alert-success',
    	messages.WARNING: 'alert-warning',
    	messages.ERROR: 'alert-danger',
    }

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'theme/templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                "debug": DEBUG,
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.messages.context_processors.messages',
                ],
                "string_if_invalid": '<< MISSING VARIABLE "%s" >>' if DEBUG else "",
            },
        },
    ]
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'stderr': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, "debug.log"),
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'pika': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
            },
        },
        'root': {
            'handlers': ['stderr'],
            'level': 'INFO',
        },
    }
