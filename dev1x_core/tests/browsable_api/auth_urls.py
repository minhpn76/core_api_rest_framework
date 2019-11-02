from __future__ import unicode_literals

from django.conf.urls import include, url

from .views import MockView

urlpatterns = [
    url(r'^$', MockView.as_view()),
    url(r'^auth/', include('mind_core.urls', namespace='mind_core')),
]
