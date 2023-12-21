from django.urls import path
from .views import SensorListCreateView, MeasurementListCreateView, SensorRetrieveUpdateAPIView


urlpatterns = [
    path('sensors/<pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('sensors/', SensorListCreateView.as_view()),
    path('measurements/', MeasurementListCreateView.as_view()),
]
