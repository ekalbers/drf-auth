from django.urls import path
from .views import FoodList, FoodDetail

urlpatterns = [
    path('', FoodList.as_view(), name='thing_list'),
    path('<int:pk>', FoodDetail.as_view(), name='things_detail'),
]
