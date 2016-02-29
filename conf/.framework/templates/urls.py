from django.conf.urls import patterns, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from core.utils.renderutils import render_to

admin.autodiscover()


@render_to('index.html')
def default_view(request):
    return {}

urlpatterns = patterns(
    '',
    (r'^__admin__/', include(admin.site.urls)),
    (r'^/?$', 'urls.default_view'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if not settings.DEBUG:
    # Coz django refuses to serve static files when debug is turned off
    # Talk to the hand
    urlpatterns += patterns(
        '',
        (r'static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )
