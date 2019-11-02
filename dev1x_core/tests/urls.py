"""
URLConf for test suite.

We need only the docs urls for DocumentationRenderer tests.
"""
from django.conf.urls import url

from mind_core.compat import coreapi
from mind_core.documentation import include_docs_urls

if coreapi:
    urlpatterns = [
        url(r'^docs/', include_docs_urls(title='Test Suite API')),
    ]
else:
    urlpatterns = []
