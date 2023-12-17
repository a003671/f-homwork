from django.db import models


class Sensor(models.Model):
    '''Датчик на котором проводят измерения.'''

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    measurements = models.TextField(blank=True)
 
 
class Measurement(models.Model):
    '''Измерение температуры на датчике.'''

    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)