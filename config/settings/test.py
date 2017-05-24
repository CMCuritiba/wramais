# -*- coding: utf-8 -*-
'''
Test settings

- Used to run tests fast on the continuous integration server and locally
'''

from .base import *  # noqa
import environ, os


# DEBUG
# ------------------------------------------------------------------------------
# Turn debug off so tests run faster
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = False

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('SECRET_KEY_LOCAL', default='')

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# In-memory email backend stores messages in django.core.mail.outbox
# for unit testing purposes
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# CACHING
# ------------------------------------------------------------------------------
# Speed advantages of in-memory caching without having to run Memcached
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'


# PASSWORD HASHING
# ------------------------------------------------------------------------------
# Use fast password hasher so tests run faster
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# TEMPLATE LOADERS
# ------------------------------------------------------------------------------
# Keep templates in memory so tests run faster
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ['django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ], ],
]

# LDAP
# ------------------------------------------------------------------------------
LDAP_AUTH_URL = env('LDAP_AUTH_URL', default='')
LDAP_AUTH_SEARCH_BASE = env('LDAP_AUTH_SEARCH_BASE', default='')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'ldap': {
        'ENGINE': 'ldapdb.backends.ldap',
        'NAME': env('LDAP_AUTH_URL'),
     },
    'default': env.db_url('DATABASE_TEST_URL'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True



