from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from mind_core.routers import DefaultRouter
from mind_core.authtoken import views
from .users.views import UserViewSet, UserCreateViewSet, TestView
from mind_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('mind_core.urls', namespace='mind_core')),
    path('sign-in/', obtain_jwt_token),
    path('sign-up/', include('mind_auth.registration.urls')),
    path('api-test/', TestView.as_view(), name="api-test"),


    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
