from django.conf import settings

from mind_core.permissions import AllowAny
from mind_auth.registration.serializers import (
    RegisterSerializer as DefaultRegisterSerializer)
from ..utils import import_callable


serializers = getattr(settings, 'mind_auth_REGISTER_SERIALIZERS', {})

RegisterSerializer = import_callable(
    serializers.get('REGISTER_SERIALIZER', DefaultRegisterSerializer))


def register_permission_classes():
    permission_classes = [AllowAny, ]
    for klass in getattr(settings, 'mind_auth_REGISTER_PERMISSION_CLASSES', tuple()):
        permission_classes.append(import_callable(klass))
    return tuple(permission_classes)
