import os

SITE_NAME = os.environ['DJANGO_SITE_NAME']

if not SITE_NAME:
    raise EnvironmentError('DJANGO_SITE_NAME not found in environment')
