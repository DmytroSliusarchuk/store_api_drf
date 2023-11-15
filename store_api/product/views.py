from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView
from .models import Product, Color, Size
from .serializers import ProductSerializer, ColorSerializer, SizeSerializer


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all().prefetch_related('colors', 'sizes')
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveDestroyAPIView):
    queryset = Product.objects.all().prefetch_related('colors', 'sizes')
    serializer_class = ProductSerializer


class ColorListView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorDetailView(RetrieveDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class SizeListView(ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer


class SizeDetailView(RetrieveDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
