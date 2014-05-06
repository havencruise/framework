from django import template
from django.conf import settings


if 'pipeline' in settings.INSTALLED_APPS:
    template.add_to_builtins('pipeline.templatetags.compressed')