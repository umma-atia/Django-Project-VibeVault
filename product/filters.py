from django_filters.rest_framework import FilterSet
from product.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category__name': ['exact'],
            'price': ['gt', 'lt'],
            'size' : ['exact'],
            'color' : ['exact'],
            'popularity' : ['exact']
        }