from rest_framework import serializers
from .models import (
    Axis,
    Institution,
    Measure
)


class MeasureSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Measure
        fields = '__all__'


class AxisSerializer(serializers.HyperlinkedModelSerializer):
    measures = MeasureSerializer(many=True, read_only=True)

    class Meta:
        model = Axis
        fields = '__all__'


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Institution
        fields = '__all__'
