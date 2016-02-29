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

sitename = os.path.dirname(os.path.abspath(__file__)).split('/')[-1]
sys.path += ['../apps', '../conf', '..']
settings_mod = '%s.settings' % sitename

try:
    __import__(settings_mod)
    from django.core.wsgi import get_wsgi_application
except ImportError:
    import sys
    sys.stderr.write("""Error:
        Can't find the file settings module. It appears you've customized things.\n
        You'll have to run django-admin.py, passing it your settings module.\n """)
    sys.exit(1)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_mod)
application = get_wsgi_application()
