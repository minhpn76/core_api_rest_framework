from __future__ import unicode_literals

from django.conf.urls import url
from django.test import TestCase
from django.test.utils import override_settings

from mind_core import serializers
from mind_core.generics import ListCreateAPIView
from mind_core.renderers import BrowsableAPIRenderer


class NestedSerializer(serializers.Serializer):
    one = serializers.IntegerField(max_value=10)
    two = serializers.IntegerField(max_value=10)


class NestedSerializerTestSerializer(serializers.Serializer):
    nested = NestedSerializer()


class NestedSerializersView(ListCreateAPIView):
    renderer_classes = (BrowsableAPIRenderer, )
    serializer_class = NestedSerializerTestSerializer
    queryset = [{'nested': {'one': 1, 'two': 2}}]


urlpatterns = [
    url(r'^api/$', NestedSerializersView.as_view(), name='api'),
]


class DropdownWithAuthTests(TestCase):
    """Tests correct dropdown behaviour with Auth views enabled."""

    @override_settings(ROOT_URLCONF='tests.browsable_api.test_browsable_nested_api')
    def test_login(self):
        response = self.client.get('/api/')
        assert 200 == response.status_code
        content = response.content.decode('utf-8')
        assert 'form action="/api/"' in content
        assert 'input name="nested.one"' in content
        assert 'input name="nested.two"' in content
