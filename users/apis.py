from itertools import chain
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
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
        persons = [PersonSerializer(
            instance=p, context={'request': request}).data for p in Person.objects.all()]
        organisations = [OrganisationSerializer(
            instance=o, context={'request': request}).data for o in Organisation.objects.all()]
        queryset = list(chain(persons, organisations))

        return Response(queryset)

    def retrieve(self, request, pk=None):
        queryset = Subject.objects.all()
        subject = get_object_or_404(queryset, pk=pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
