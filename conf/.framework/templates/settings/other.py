CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# In the case where SITE_ID is present, ignore this warning
# SILENCED_SYSTEM_CHECKS = [
#     '1_6.W001'  # Silences some project unit tests
# ]