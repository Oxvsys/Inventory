from django.contrib import admin

from inventory import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "type", "visible", "discount")
    list_filter = ("type", "visible")
    list_editable = ("price", "visible", "discount")
