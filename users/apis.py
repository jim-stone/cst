from itertools import chain
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions, mixins, viewsets
from .serializers import (
    UserSerializer, InstitutionalRoleSerializer,
    SubjectSerializer, PersonSerializer, OrganisationSerializer
)
from .models import (
    CstUser as User, InstitutionalRole,
    Person, Organisation, Subject
)


class UserViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class InstitutionalRoleViewset(viewsets.ModelViewSet):
    queryset = InstitutionalRole.objects.all()
    serializer_class = InstitutionalRoleSerializer
    permission_classes = [permissions.IsAdminUser]


class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAdminUser]


class OrganisationViewset(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [permissions.IsAdminUser]


class SubjectViewset(viewsets.ViewSet):

    permission_classes = [permissions.IsAdminUser]

    def list(self, request):
        persons = PersonSerializer(
            Person.objects.all(), many=True, context={'request': request})
        organisations = OrganisationSerializer(
            Organisation.objects.all(), many=True, context={'request': request})
        queryset = list(chain(persons.data, organisations.data))
        return Response(queryset)

    def retrieve(self, request, pk=None):
        serializer_class = OrganisationSerializer

        try:
            subject = Organisation.objects.get(subject_ptr_id=pk)
        except ObjectDoesNotExist:
            queryset = Person.objects.all()
            serializer_class = PersonSerializer
            subject = get_object_or_404(queryset, subject_ptr_id=pk)

        serializer = serializer_class(
            subject, context={'request': request})
        return Response(serializer.data)
