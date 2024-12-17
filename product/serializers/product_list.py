from rest_framework import serializers


class ProductListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, default="")
    category = serializers.CharField(max_length=100, default="")
    order_by = serializers.CharField(max_length=20, default="created_at")
    page = serializers.IntegerField(default=1)
    page_size = serializers.IntegerField(default=10)

    def validate_order_by(self, value):
        allowed_values = ["category", "created_at"]

        
        if (value not in allowed_values):
            raise serializers.ValidationError(f"Allowed values are: {', '.join(allowed_values)}.")
        
        return value
   
