from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest.serializers import UserSerializer

from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	# permission_classes = [permissions.IsAuthenticated]