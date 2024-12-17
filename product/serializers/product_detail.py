from rest_framework import serializers


class ProductDetailSerializer(serializers.Serializer):
   id = serializers.IntegerField()

    
