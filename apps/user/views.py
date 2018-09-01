from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.user.serialzer import UserSerializer


class LoginViewSet(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id
        })

class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer
    model = User
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
