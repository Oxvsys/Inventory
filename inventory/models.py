from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    type = models.CharField(max_length=255)
    visible = models.BooleanField(default=False)
    discount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
