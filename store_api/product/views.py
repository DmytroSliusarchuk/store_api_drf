from rest_framework.generics import RetrieveDestroyAPIView, ListCreateAPIView, ListAPIView
from .models import Product, Color, Size
from .serializers import ProductSerializer, ColorSerializer, SizeSerializer, ProductGeneralSerializer


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all().prefetch_related('colors', 'sizes')
    serializer_class = ProductSerializer

class ProductGeneralListView(ListAPIView):
    serializer_class = ProductGeneralSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        limit = self.request.query_params.get('limit', None)

        if limit is not None and limit.isdigit():
            limit = int(limit)
            queryset = queryset[:limit]

        color = self.request.query_params.get('color', None)
        size = self.request.query_params.get('size', None)

        if color is not None and color.isdigit():
            queryset = queryset.filter(colors__id=color)

        if size is not None and size.isdigit():
            queryset = queryset.filter(sizes__id=size)

        return queryset


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
