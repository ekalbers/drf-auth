from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Food
from .serializer import FoodSerializer
from .permissions import isOwnerOrReadOnly


class FoodList(ListAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = (isOwnerOrReadOnly,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
