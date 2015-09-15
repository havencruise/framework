from optparse import make_option
from django.conf import settings
from django.core.management.base import AppCommand, CommandError
import os
import shutil

STATIC_DIRS = ['js', 'css', 'img', 'swf']

WINDOWS = False
if os.name in ('nt', 'dos'):
    WINDOWS = True


class Command(AppCommand):

    option_list = AppCommand.option_list + (
        make_option('--force', action='store_true', dest='force', default=False,
                    help='Remove existing files and copy app static files again.'),
        )

    help = "Copies any app's specific static files over to static_root directory"
    args = '[appname1, appname2, ...]'

    def handle_app(self, app, **options):

        verbosity = int(options.get('verbosity'))

        app_static_dir = "%s/static/%s" % (
                            "/".join(app.__file__.split('/')[:-1]),
                            app.__package__)
        if WINDOWS:
            app_static_dir = "%s\\static\\%s" % (
                                "\\".join(app.__file__.split('\\')[:-1]),
                                app.__package__)

        app_name = app.__name__
        static_dir = '%s/%s' % (settings.STATIC_ROOT, app_name)

        if not os.path.exists(app_static_dir):
            if verbosity > 0:
                print 'App %s does not have a static directory' % (app_name)
            return

        force = options.get('force')

        if os.path.exists(static_dir) and force:
            shutil.rmtree(static_dir)

        if os.path.exists(static_dir):
            if verbosity > 0:
                print 'Static directory %s already exists in %s' % (
                    app_name, settings.STATIC_ROOT)
        else:
            os.mkdir(static_dir)
            for i in STATIC_DIRS:
                if WINDOWS:
                    if os.path.exists("%s\\%s" % (app_static_dir, i)):
                        print "Copying %s\\%s to %s" % (
                            app_static_dir, i, static_dir)
                        shutil.copytree("%s\\%s" % (app_static_dir, i),
                                        "%s\\%s" % (static_dir, i),
                                        ignore=shutil.ignore_patterns('.svn'))
                else:
                    if os.path.exists("%s/%s" % (app_static_dir, i)):
                        print "Copying %s/%s to %s" % (app_static_dir, i, static_dir)
                        shutil.copytree("%s/%s" % (app_static_dir, i),
                                        "%s/%s" % (static_dir, i),
                                        ignore=shutil.ignore_patterns('.svn'))
