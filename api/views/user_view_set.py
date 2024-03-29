from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from rest_framework import generics, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.serializers.user_serializer import UserSerializer
from api.views.common import ConnectionValidations


class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated)
    authentication_class = [JSONWebTokenAuthentication, OAuth2Authentication]
    queryset = (
        User.objects.all().cache(ops=["get", "fetch"], timeout=60 * 30)
        if ConnectionValidations.redis_connection_validation()
        else User.objects.all()
    )
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated)
    authentication_class = [JSONWebTokenAuthentication, OAuth2Authentication]
    queryset = (
        User.objects.all().cache(ops=["get", "fetch"], timeout=60 * 30)
        if ConnectionValidations.redis_connection_validation()
        else User.objects.all()
    )
    serializer_class = UserSerializer
