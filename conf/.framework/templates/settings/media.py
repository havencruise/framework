import os

SITE_NAME = os.environ['DJANGO_SITE_NAME']
APP_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(APP_ROOT, SITE_NAME, 'upload')
STATIC_ROOT = os.path.join(APP_ROOT, SITE_NAME, 'static')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/upload/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(APP_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

ADMIN_MEDIA_PREFIX = '/media/'
