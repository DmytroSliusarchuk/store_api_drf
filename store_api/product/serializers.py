from rest_framework import serializers
from .models import Color, Size, Product

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True, read_only=True)
    sizes = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'image', 'colors', 'sizes']
