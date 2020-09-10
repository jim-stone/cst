from rest_framework import (
    authentication,
    permissions,
    viewsets
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Axis,
    Institution,
    Measure
)

from .serializers import (
    AxisSerializer,
    MeasureSerializer,
    InstitutionSerializer)

from .enumerations import Programme


class InstitutionViewset(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class AxisViewset(viewsets.ModelViewSet):
    queryset = Axis.objects.all()
    serializer_class = AxisSerializer


class MeasuresViewset(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer


class ProgrammeViewset(viewsets.ViewSet):
    def list(self, request):
        return Response(Programme.to_dict())


class ListPWDViewset(viewsets.ViewSet):
    def list(self, request):
        programmes = Programme.to_dict()
        axes = Axis.objects.all()
        programmes_result = {}
        for programme_key in programmes:
            axes_result = {}
            programmes_result[programmes[programme_key]] = axes_result
            for axis in axes:
                print(axis.get_programme_display())
                if axis.get_programme_display() == programmes[programme_key]:
                    programmes_result[programmes[programme_key]].update(
                        {str(axis): [str(m) for m in axis.measures.all()]})

        return Response(programmes_result)
