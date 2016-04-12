# -*- coding: utf-8 -*-
import os
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))

SITE_NAME = os.environ['DJANGO_SITE_NAME']

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(APP_ROOT, SITE_NAME, 'templates'),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            "django.contrib.auth.context_processors.auth",
            "django.template.context_processors.debug",
            "django.template.context_processors.i18n",
            "django.template.context_processors.media",
            "django.template.context_processors.static",
            "django.template.context_processors.request",
            "django.template.context_processors.csrf",
        ],
        "debug": True
    }
}]
