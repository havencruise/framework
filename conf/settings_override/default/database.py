# This can be overridden in the environment specific files

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.mysql',

        # Or path to database file if using sqlite3.
        'NAME': '',

        # Not used with sqlite3.
        'USER': '',

        # Not used with sqlite3.
        'PASSWORD': '',

        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',

        # Set to empty string for default. Not used with sqlite3.
        'PORT': '',
    }
}
