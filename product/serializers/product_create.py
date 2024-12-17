from rest_framework import serializers


class ProductCreateSerializer(serializers.Serializer):
    """
    Serializer for creating a Product.
    """
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    cost_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    selling_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category = serializers.CharField(max_length=100)
    stock_available = serializers.IntegerField(default=0)
    customer_rating = serializers.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    units_sold = serializers.IntegerField(default=0)
    demand_forecast  = serializers.IntegerField(default=None)


    def validate_customer_rating(self, value):
        """
        Validate customer_rating to ensure it's within the allowed range.
        """
        if not (0 <= value <= 5):
            raise serializers.ValidationError("Customer rating must be between 0 and 5.")
        return value
