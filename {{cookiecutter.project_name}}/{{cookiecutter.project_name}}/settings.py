import os
from configurations import Configuration, values


class Common(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = values.SecretValue()
    DEBUG = False
    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'debug_toolbar',
        'raven.contrib.django.raven_compat',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    ROOT_URLCONF = '{{ cookiecutter.project_name }}.urls'

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

    WSGI_APPLICATION = '{{ cookiecutter.project_name }}.wsgi.application'

    DATABASES = values.DatabaseURLValue(
        # django-configurations maps this to the caster (which is dj_database_url)
        default='postgres://localhost/{{ cookiecutter.project_name }}',
        conn_max_age=500,
    )

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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'Europe/Berlin'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_ROOT = os.path.join(BASE_DIR, '_static')
    STATIC_URL = values.Value(default='/static/', environ_prefix='')

    RAVEN_CONFIG = {
        'dsn': values.Value(environ_name='SENTRY_DSN', environ_prefix='', default=''),
        'release': values.Value(environ_name='HEROKU_RELEASE_VERSION', environ_prefix='',
                                default=''),
    }


class Prod(Common):
    pass


class Dev(Common):
    DEBUG = True
