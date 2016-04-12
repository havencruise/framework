from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views import static as static_views
from core.utils.renderutils import render_to

admin.autodiscover()


@render_to('index.html')
def default_view(request):
    return {}

urlpatterns = [
    url(r'^__admin__/', include(admin.site.urls)),
    url(r'^$', default_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if not settings.DEBUG:
    # Coz django refuses to serve static files when debug is turned off
    # Talk to the hand
    urlpatterns += [
        url(r'static/(?P<path>.*)$', static_views.serve,
            {'document_root': settings.STATIC_ROOT}),
    ]
