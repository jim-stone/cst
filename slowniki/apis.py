from rest_framework import (
    authentication, permissions, viewsets, status
)
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework import serializers
from .models import Dictionary, EntryFieldSpecification
from .services import create_dictionary, create_dictionary_specification


class DictionariesListApiViewset (ReadOnlyModelViewSet):
    class OutputSerializer(serializers.HyperlinkedModelSerializer):

        class SpecificationSerializer(serializers.ModelSerializer):
            class Meta:
                model = EntryFieldSpecification
                fields = ['name', 'isReference', 'ReferencedDict']

        field_specs = SpecificationSerializer(many=True)

        class Meta:
            model = Dictionary
            fields = '__all__'

    serializer_class = OutputSerializer
    queryset = Dictionary.objects.all()
    permission_classes = []


class DictionaryCreateApi (ModelViewSet):
    class InputSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Dictionary
            fields = ['id', 'name', 'isHorizontal', 'isModifiable', 'isExtensible']

    serializer_class = InputSerializer
    queryset = Dictionary.objects.all()
    allowed_methods = ['GET', 'POST', 'DELETE']

    def create(self, request):
        creator = request.user.username
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_obj_id = create_dictionary(
            target_dict=serializer.data, creator_name=creator)
        return Response(new_obj_id, status=status.HTTP_201_CREATED)


class EntryFieldSpecificationApi (ModelViewSet):
    class InputSerializer (serializers.HyperlinkedModelSerializer):
        class Meta:
            model = EntryFieldSpecification
            fields = [
                'dictionaryId',
                'order',
                'name',
                'type',
                'isReference',
                'ReferencedDict',
                'isUnique',
                'uniqueGroupNumber',
                'defaultValue',
                'isOptional'
            ]

    serializer_class = InputSerializer
    queryset = EntryFieldSpecification.objects.all()
    allowed_methods = ['POST']

    def create(self, request):
        creator = request.user.username
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_obj_id = create_dictionary_specification(
            target_dict=serializer.data, creator_name=creator)

        return Response(new_obj_id, status=status.HTTP_201_CREATED)
