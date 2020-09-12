from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import UserSerializer
from .models import CstUser as User


class UserViewset(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
