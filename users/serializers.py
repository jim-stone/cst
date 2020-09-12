from rest_framework import serializers
from .models import CstUser as User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
