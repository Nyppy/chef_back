from django.http import JsonResponse
from rest_framework import viewsets

from . import models, serializers


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()

    def list(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return JsonResponse({
            'request': 'request of this type is prohibited'
        }, status=200)

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return JsonResponse({'request': 'success'})
