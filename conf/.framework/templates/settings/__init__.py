
settings_files = ('app', 'auth', 'email', 'database', 'locale', 'log', 'media',
                  'storage', 'other', 'template')

try:
    from settings._generated_settings import *
except:
    # Settings are not generated
    # Go through current directory, then environment
    import os
    import sys

    env = os.environ['DJANGO_ENVIRONMENT']

    if env is None:
        raise EnvironmentError('DJANGO_ENVIRONMENT not set')

    locations = ('settings', 'settings_override.env.%s' % env)

    for loc in locations:
        for settings_file in settings_files:
            try:
                module_name = '%s.%s' % (loc, settings_file)
                __import__(module_name)
                module = sys.modules[module_name]

                for setting in dir(module):
                    if setting == setting.upper():
                        try:
                            val = getattr(module, setting, None)
                            if isinstance(val, basestring):
                                exec("%s = '%s'" % (setting, val))
                            else:
                                exec("%s = %s" % (setting, val))
                        except Exception, e:
                            pass
            except Exception, e:
                pass
