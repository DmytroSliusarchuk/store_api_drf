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
    colors_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Color.objects.all(), write_only=True)
    sizes_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Size.objects.all(), write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'image', 'colors', 'colors_id', 'sizes', 'sizes_id']

    def create(self, validated_data):
        colors_data = validated_data.pop('colors_id', [])
        sizes_data = validated_data.pop('sizes_id', [])
        product = Product.objects.create(**validated_data)
        product.colors.set(colors_data)
        product.sizes.set(sizes_data)

        return product


class ProductGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image']
