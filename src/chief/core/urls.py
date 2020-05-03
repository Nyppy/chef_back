from django.conf.urls import url, include
from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('order', views.OrderViewSet)
router.register('categories', views.CategoriesViewSet)
router.register('dish', views.DishViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
    path('stop-list/', views.ViewStopList.as_view(), name='stop-list'),
    path('get-dish/', views.GetDish.as_view(), name='get-dish'),  # тоже убоать надо будет
    path('get-categories/', views.Categories.as_view(), name='get-categories'),  # потом уберу
]