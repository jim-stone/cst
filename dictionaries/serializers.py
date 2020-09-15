from rest_framework import serializers
from .models import (Axis, Measure, Programme, Pwd
                     )


class PwdSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pwd
        fields = '__all__'


class ProgrammeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Programme
        fields = '__all__'


class MeasureSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Measure
        fields = '__all__'


class AxisSerializer(serializers.HyperlinkedModelSerializer):
    measures = MeasureSerializer(many=True, read_only=True)

    class Meta:
        model = Axis
        fields = '__all__'
