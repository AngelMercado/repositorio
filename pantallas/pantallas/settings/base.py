"""
Django settings for pantallas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...) 
# os was rempalced to unipath for personality use
from unipath import Path
import os
BASE_DIR = Path(__file__).ancestor(3)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3h=iz%a+b=c+6k3mgvndc2l$m7k!_&_8(oud^ktva1hw82idhu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition
DJANGO_APPS = (
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_PARTY_APPS = (
'south',
'djrill',
'django_extensions',
)
LOCAL_APPS = (
# OWN DEVELOPED APPS
'apps.home',
'apps.careers',
'apps.academics',
'apps.vacancies',
'apps.events',
'apps.gripbox'
) 
#ALL APPS
INSTALLED_APPS = DJANGO_APPS+THIRD_PARTY_APPS+LOCAL_APPS 

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pantallas.urls'

WSGI_APPLICATION = 'pantallas.wsgi.application'

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'

MANDRILL_API_KEY='XuKUcrxHNJSZyc4ESi-06Q'