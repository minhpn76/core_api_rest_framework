from django.conf.urls import url
from django.http import HttpResponse
from mind_core import permissions
from mind_core.views import APIView
try:
    from mind_core_oauth.authentication import OAuth2Authentication
except ImportError:
    try:
        from mind_core.authentication import OAuth2Authentication
    except ImportError:
        OAuth2Authentication = None

from mind_jwt import views
from mind_jwt.authentication import JSONWebTokenAuthentication


class MockView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return HttpResponse('mockview-get')

    def post(self, request):
        return HttpResponse('mockview-post')


urlpatterns = [
    url(r'^auth-token/$', views.obtain_jwt_token),
    url(r'^auth-token-refresh/$', views.refresh_jwt_token),
    url(r'^auth-token-verify/$', views.verify_jwt_token),

    url(r'^jwt/$', MockView.as_view(
        authentication_classes=[JSONWebTokenAuthentication])),
    url(r'^jwt-oauth2/$', MockView.as_view(
        authentication_classes=[
            JSONWebTokenAuthentication, OAuth2Authentication])),
    url(r'^oauth2-jwt/$', MockView.as_view(
        authentication_classes=[
            OAuth2Authentication, JSONWebTokenAuthentication])),
]
