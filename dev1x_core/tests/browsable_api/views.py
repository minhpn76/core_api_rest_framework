from __future__ import unicode_literals

from mind_core import authentication, renderers
from mind_core.response import Response
from mind_core.views import APIView


class MockView(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes = (renderers.BrowsableAPIRenderer, renderers.JSONRenderer)

    def get(self, request):
        return Response({'a': 1, 'b': 2, 'c': 3})
