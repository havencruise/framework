from django.conf.urls import patterns, url, include
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib import admin
admin.autodiscover()

# def default_view(request):
#     return HttpReponse('{}', 
#             mimetype='application/json')


def the_default_view(request):
    return render(request, 
            'base/index.html', {})

urlpatterns = patterns(
    (r'^$', 'urls.the_default_view'),
    (r'^__admin__/', include(admin.site.urls)),
)