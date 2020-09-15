from rest_framework import serializers
from .models import CstUser as User, InstitutionalRole, Subject, Person, Organisation
from dictionaries.models import Pwd
from dictionaries.serializers import PwdSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['url', 'firstname', 'lastname', 'pesel', 'foreign_id']


class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ['url', 'name', 'kind', 'nip', 'foreign_id', 'superior']


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    persons = PersonSerializer(many=True, read_only=True)
    organisations = OrganisationSerializer(many=True, read_only=True)
    # managing_person = UserSerializer()

    class Meta:
        model = Subject
        fields = ['id', 'managing_person', 'persons', 'organisations']


class InstitutionalRoleSerializer(serializers.HyperlinkedModelSerializer):
    # pwd = PwdSerializer()
    # org = OrganisationSerializer()

    class Meta:
        model = InstitutionalRole
        fields = '__all__'
