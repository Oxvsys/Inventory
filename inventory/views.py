from rest_framework import generics, status
from rest_framework.response import Response

from inventory import models, serializers


class ProductView(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
