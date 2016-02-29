import os
import sys
import warnings
warnings.warn(
    "Please use conf/deployment/wsgi for deployment purposes",
    DeprecationWarning)

try:
    if not os.environ['DJANGO_ENVIRONMENT']:
        os.environ['DJANGO_ENVIRONMENT'] = 'local'
except:
    os.environ['DJANGO_ENVIRONMENT'] = 'local'

os.environ['DJANGO_SITE_NAME'] = os.path.dirname(
    os.path.abspath(__file__)).split('/')[-1]

sys.path += ['../apps', '../conf', '%s' % os.environ['DJANGO_SITE_NAME']]
settings_mod = '%s.settings' % os.environ['DJANGO_SITE_NAME']
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_mod)

try:
    __import__(settings_mod)
    from django.core.wsgi import get_wsgi_application
except ImportError:
    import sys
    sys.stderr.write("""Error:
        Can't find the 'settings.py' or 'settings' module.
        It appears you've customized things.You'll have to run django-admin.py,
        passing it your settings module.(If the file settings.py does indeed exist,
        it's causing an ImportError somehow.)\n""")
    sys.exit(1)

application = get_wsgi_application()
