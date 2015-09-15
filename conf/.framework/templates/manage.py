#!/usr/bin/env python
import sys
import os
import importlib

for i in sys.argv:
    if i.startswith('--env'):
        env = i.split('=')[1]
        sys.argv.remove(i)
        os.environ['DJANGO_ENVIRONMENT'] = env
        break

if os.name in ("nt", "dos"):
    os.environ['DJANGO_SITE_NAME'] = os.path.dirname(os.path.abspath(__file__)).split('\\')[-1]
else:
    os.environ['DJANGO_SITE_NAME'] = os.path.dirname(os.path.abspath(__file__)).split('/')[-1]

project_name = os.environ['DJANGO_SITE_NAME']

try:
    if not os.environ['DJANGO_ENVIRONMENT']:
        os.environ['DJANGO_ENVIRONMENT'] = 'local'
except:
    os.environ['DJANGO_ENVIRONMENT'] = 'local'


sys.path += ['../apps', '../conf', '.']


try:
    import settings  # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("""
        Error: Can't find the file 'settings.py' in the directory containing %r.
        It appears you've customized things.\n
        You'll have to run django-admin.py, passing it your settings module.\n
        (If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n""" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    execute_from_command_line()
