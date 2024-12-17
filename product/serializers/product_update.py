from rest_framework import serializers

class ProductUpdateSerializer(serializers.Serializer):
    """
    Serializer for updating a Product.
    """
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    cost_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    selling_price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    category = serializers.CharField(max_length=100, required=False)
    stock_available = serializers.IntegerField(required=False)
    customer_rating = serializers.DecimalField(max_digits=3, decimal_places=2, default=0.0, required=False)
    units_sold = serializers.IntegerField(default=0, required=False)

