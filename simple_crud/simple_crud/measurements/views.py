from rest_framework.viewsets import ModelViewSet

from .models import Measurement, Sensor
from measurements.serializers import MeasurementSerializer, SensorDetailSerializer

class SensorViewSet(ModelViewSet):
    '''ViewSet для датчика.'''
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementViewSet(ModelViewSet):
    '''ViewSet для измерения.'''
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

