from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from inventory import models


class ProductBulkCreateUpdateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        product_data = [models.Product(**item) for item in validated_data]
        return models.Product.objects.bulk_create(product_data)

    def update(self, instance, validated_data):
        instance_hash = {index: i for index, i in enumerate(instance)}
        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]
        writable_fields = [
            x
            for x in self.child.Meta.fields
            if x not in self.child.Meta.read_only_fields
        ]

        try:
            self.child.Meta.model.objects.bulk_update(result, writable_fields)
        except IntegrityError as e:
            raise ValidationError(e)

        return result


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["id", "title", "description", "price", "type", "visible", "discount", "created_at", "updated_at"]
        read_only_fields = ['id', ]
        list_serializer_class = ProductBulkCreateUpdateSerializer
