from rest_framework import serializers
from inventory import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["id", "title", "description", "price", "type", "visible", "discount", "created_at", "updated_at"]
