from rest_framework import serializers

from app_products.models import Product


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ["name", "price"]

