from django.conf import settings

from mind_core.authtoken.models import Token as DefaultTokenModel

from .utils import import_callable

# Register your models here.

TokenModel = import_callable(
    getattr(settings, 'mind_auth_TOKEN_MODEL', DefaultTokenModel))
