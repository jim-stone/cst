from rest_framework import (
    authentication, permissions, viewsets
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Axis, Measure, Programme, Pwd
)

from .serializers import (
    AxisSerializer,
    MeasureSerializer,
    ProgrammeSerializer,
    PwdSerializer
)


class AxisViewset(viewsets.ModelViewSet):
    queryset = Axis.objects.all()
    serializer_class = AxisSerializer


class MeasuresViewset(viewsets.ModelViewSet):
    queryset = Measure.objects.all()
    serializer_class = MeasureSerializer


class ProgrammeViewset(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer


class PwdViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Pwd.objects.all()
    serializer_class = PwdSerializer
    permission_classes = [permissions.IsAdminUser]


class ListPWDViewset(viewsets.ViewSet):
    def list(self, request):
        programmes = Programme.objects.all()
        axes = Axis.objects.all()
        if programmes:
            programmes_result = {}
            for programme in programmes:
                axes_result = {}
                prog_name = f'{programme.code}.{programme.name}'
                programmes_result[prog_name] = axes_result
                for axis in axes:
                    if axis.prog == programme:
                        programmes_result[prog_name].update(
                            {str(axis): [str(m) for m in axis.measures.all()]})
            return Response(programmes_result)
        return Response('Brak poziomów wdrazania')
