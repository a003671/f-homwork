from urllib import response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .filters import AdvertisementFilter

from .permissions import IsOwnerOrReadOnly

from .serializers import AdvertisementSerializer

from .models import Advertisement


class AdvertisementViewSet(ModelViewSet):
    '''ViewSet для объявлений.'''
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['creator', 'status']
    pagination_class = 'rest_framework.pagination.PageNumberPagination'

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        return []

    def list(self, request, **kwargs):
        queryset = Advertisement.objects.all()
        queryset = AdvertisementFilter(data=request.GET, queryset=queryset, request=request).qs
        serializer = AdvertisementSerializer(queryset, many=True)
        return response(serializer.data)