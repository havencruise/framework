import os

BASE_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    '../../../'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Your Name', 'email@gmail.com'),
)

MANAGERS = ADMINS

SITE_NAME = os.environ['DJANGO_SITE_NAME']

# MIDDLEWARE_CLASSES should in <site_name>.settings.app.py file
# INSTALLED_APPS should be in <site_name>.settings.app.py file

ROOT_URLCONF = SITE_NAME + '.urls'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
