from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.views import View
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

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


class DishViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DishSerializer
    queryset = models.DishObjects.objects.all()
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(img=self.request.data.get('img'))

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


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriesSerializer
    queryset = models.Categories.objects.all()

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return JsonResponse({'request': 'success'})


class Categories(View):

    def get(self, request):
        data = models.Categories.objects.all()

        return JsonResponse({'data': [{'id': category.id, 'name': category.name} for category in data]})


class GetDish(View):

    def get(self, request):

        data = models.DishObjects.objects.all()

        dish = []

        for i in data:
            if i.availability:
                dish.append(
                    {
                        'categories_id': i.categories.pk,
                        'categories_name': i.categories.name,
                        'name': i.name,
                        'id': i.pk,
                        'cal': i.cal,
                        'fats': i.fats,
                        'carbo': i.carbo,
                        'prot': i.prot,
                        'price': i.price,
                        'img': i.img
                    }
                )

        return JsonResponse({'data': dish})


@method_decorator(csrf_exempt, name='dispatch')
class ViewStopList(View):

    def get(self, request):
        data = models.DishObjects.objects.all()
        list_data = {'data': []}

        for i in data:
            if not i.availability:
                list_data['data'].append({
                    'categories_id': i.categories.pk,
                    'categories_name': i.categories.name,
                    'name': i.name,
                    'id': i.pk,
                })

        return JsonResponse(list_data)

    def post(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            print(data, type(data))
            # {'dish_add': [2,3,5], 'dish_del': []}
            if len(data['dish_add']) > 0:
                for i in data['dish_add']:
                    dish = models.DishObjects.objects.get(pk=i)
                    dish.availability = False
                    dish.save()
            if len(data['dish_del']) > 0:
                for i in data['dish_del']:
                    dish = models.DishObjects.objects.get(pk=i)
                    dish.availability = True
                    dish.save()

            return JsonResponse({'added': True})

