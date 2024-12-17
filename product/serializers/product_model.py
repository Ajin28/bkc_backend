from rest_framework import serializers
from common.models import Product

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =  '__all__'
