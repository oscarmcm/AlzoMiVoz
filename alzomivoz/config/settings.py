# -*- coding: utf-8 -*-
"""
Django settings for alzomivoz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from os.path import join

from configurations import Configuration, values

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(join(BASE_DIR, 'apps'))
sys.path.append(join(BASE_DIR, 'libs'))

class Common(Configuration):

    ########## APP CONFIGURATION
    DJANGO_APPS = (
        # Default Django apps:
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Useful template tags:
        # 'django.contrib.humanize',

        # Admin
        'suit',
        'django.contrib.admin',
        'django.contrib.admindocs',
    )
    THIRD_PARTY_APPS = (
        'south',
        'crispy_forms',
        'sorl.thumbnail',
        'rest_framework',
        'social_auth',
        'django_social_share',
        'twitter_tag',
    )

    # Apps specific for this project go here.
    LOCAL_APPS = (
        'denuncia',
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    #INSTALLED_APPS += (
    #    # Needs to come last for now because of a weird edge case between
    #    #   South and allauth
    #)
    ########## END APP CONFIGURATION
    APPEND_SLASH = True

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    ########## END MIDDLEWARE CONFIGURATION

    ########## DEBUG
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = values.BooleanValue(True)

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
    TEMPLATE_DEBUG = DEBUG
    ########## END DEBUG

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'onk8mo=8envufmhe1^@h^_zgiq0xspizlh_d0fjmgz%=qsymgw'

    FIXTURE_DIRS = (
        join(BASE_DIR, 'fixtures'),
    )

    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

    DATABASES = values.DatabaseURLValue('postgres://localhost/alzomivoz')

    ########## CACHING
    # Do this here because thanks to django-pylibmc-sasl and pylibmc memcacheify is painful to install on windows.
    # memcacheify is what's used in Production
    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
        }
    }
    ########## END CACHING

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    ########## GENERAL CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
    TIME_ZONE = 'America/Managua'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
    LANGUAGE_CODE = 'es-NI'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
    USE_I18N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
    USE_L10N = True

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
    USE_TZ = True
    ########## END GENERAL CONFIGURATION

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        # Your stuff: custom template context processers go here
        "social_auth.context_processors.social_auth_by_type_backends"
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )

    # See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
    CRISPY_TEMPLATE_PACK = 'bootstrap3'
    ########## END TEMPLATE CONFIGURATION

    ########## STATIC FILE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
    STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'staticfiles')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        join(BASE_DIR, 'static'),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    ########## END STATIC FILE CONFIGURATION

    ########## Your common stuff: Below this line define 3rd party libary settings
    SOUTH_MIGRATION_MODULES = {
            'taggit': 'taggit.south_migrations',
    }
    #suit config admin

    SUIT_CONFIG = {
        "ADMIN_NAME": "Alzo Mi Voz",
        'MENU_ICONS': {
            'auth': 'icon-lock',
            'news': 'icon-file',
            'treemenus': 'icon-tasks',
            'taggit': 'icon-tags',
            'sites': 'icon-globe',
            'siteconf': 'icon-edit',
        }
    }

    FILEBROWSER_SUIT_TEMPLATE = True
    FILEBROWSER_DIRECTORY = ''
    FILEBROWSER_EXTENSIONS = {
        'Folder': [''],
        'Image': ['.jpg','.jpeg','.gif','.png',],
        'Document': ['.pdf','.doc','.rtf','.txt','.xls','.csv'],
        'Video': ['.mov','.wmv','.mpeg','.mpg','.avi','.rm'],
        'Audio': ['.mp3','.mp4','.wav','.aiff','.midi','.m4p']
    }


    ########## MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(os.path.dirname(BASE_DIR), 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    ########## END MEDIA CONFIGURATION

    ########## URL Configuration
    ROOT_URLCONF = 'config.urls'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
    WSGI_APPLICATION = 'config.wsgi.application'
    ########## End URL Configuration

    ### Twitter Tags
    # Your access token: Access token
    TWITTER_OAUTH_TOKEN = '419211195-LV3eZUNEqCKpsY3XjKCoG7kC7UmODYGQTO7tQdkZ'
    # Your access token: Access token secret
    TWITTER_OAUTH_SECRET = 'xaAPkiXiyrpOI1tRKm3FvH9oSRGz5sOgvT7nulYIl4d4t'
    # OAuth settings: Consumer key
    TWITTER_CONSUMER_KEY = 'p7SKYyhbEmjQfwWiCM7pNzrl'
    # OAuth settings: Consumer secret
    TWITTER_CONSUMER_SECRET = 'Pys3c5oMqtZ8gdKfFrdmMxyqFuW5xSQnUO5mIkgRhQKlolRLNR'

    ###Backend to autentications
    AUTHENTICATION_BACKENDS = (
        'social_auth.backends.google.GoogleOAuth2Backend',
        'social_auth.backends.contrib.github.GithubBackend',
        'social_auth.backends.twitter.TwitterBackend',
        'social_auth.backends.facebook.FacebookBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

    ###Social Login URL
    LOGIN_URL = '/login/'
    LOGIN_REDIRECT_URL = '/members/'
    LOGIN_ERROR_URL = '/login-error/'

    ###social settings
    SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
    SOCIAL_AUTH_UID_LENGTH = 16
    SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
    SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
    SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
    SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
    SOCIAL_AUTH_ENABLED_BACKENDS = ('google', 'github', 'facebook', 'twitter')

    GITHUB_API_KEY = ''
    GITHUB_API_SECRET = '' 
    GOOGLE_OAUTH2_CLIENT_ID = '766134566502-sdi8mg21idcvd6eraakv08nk4ds1ekd0.apps.googleusercontent.com'
    GOOGLE_OAUTH2_CLIENT_SECRET = '97M0dS4OrXVyrOJHBb_cvVVl'
    TWITTER_CONSUMER_KEY         = 'Np7SKYyhbEmjQfwWiCM7pNzrl'
    TWITTER_CONSUMER_SECRET      = 'Pys3c5oMqtZ8gdKfFrdmMxyqFuW5xSQnUO5mIkgRhQKlolRLNR'
    FACEBOOK_APP_ID              = '355162997978167'
    FACEBOOK_API_SECRET          = '2cba20b44f27e02faf98a539fa36b653'

class Local(Common):

    ########## INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    ########## END INSTALLED_APPS

    ########## Mail settings
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    ########## End mail settings

    ########## django-debug-toolbar
    #MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    #INSTALLED_APPS += ('debug_toolbar',)

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    ########## end django-debug-toolbar
    DATABASES = values.DatabaseURLValue('sqlite://///%sdb.sqlite3' % BASE_DIR)

    ########## Your local stuff: Below this line define 3rd party libary settings

    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': ''
        }
    }

class Production(Common):

    DEBUG = True
    ########## INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    ########## END INSTALLED_APPS

    ########## SECRET KEY
    SECRET_KEY = 'onk8mo=8envufmhe1^@h^_zgiq0xspizlh_d0fjmgz%=qsymgw'
    ########## END SECRET KEY


    # set this to 60 seconds and then to 518400 when you can prove it works
    #SECURE_HSTS_SECONDS = 60
    #SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    #SECURE_FRAME_DENY = values.BooleanValue(True)
    #SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    #SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    #SESSION_COOKIE_SECURE = values.BooleanValue(False)
    #SESSION_COOKIE_HTTPONLY = values.BooleanValue(True)
    #SECURE_SSL_REDIRECT = values.BooleanValue(True)
    ########## end django-secure

    ########## SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    ########## END SITE CONFIGURATION


    ########## TEMPLATE CONFIGURATION

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        )),
    )
    ########## END TEMPLATE CONFIGURATION

    

    
