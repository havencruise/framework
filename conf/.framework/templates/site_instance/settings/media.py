import os
SITE_NAME = os.environ['DJANGO_SITE_NAME']

if not SITE_NAME:
    raise EnvironmentError, 'DJANGO_SITE_NAME not found in environment'

PIPELINE_JS = {
    'core': {
        'source_filenames': (
            'core/js/base.js',
        ),
        'output_filename': '%s/js/framework.r?.js' % SITE_NAME
    },
    'jquery' : {
        'external_urls': (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.0/jquery-ui.min.js'
        ),
        'output_filename': '%s/js/jquery.r?.js' % SITE_NAME
    }
}


PIPELINE_CSS = {
    'core': {
        'source_filenames': (
            'core/js/base.css',
         ),
        'output_filename': '%s/css/framework.r?.css' % SITE_NAME
    },
    'jquery' : {
        'external_urls': (
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.0/themes/smoothness/jquery-ui.css',
        ),
        'output_filename': '%s/css/jquery.r?.css' % SITE_NAME
    }
}
