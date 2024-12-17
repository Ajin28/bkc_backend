from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from common.models import Product
from product.serializers import ProductListSerializer, ProductModelSerializer, ProductDetailSerializer
from common.mixins.permission import IsAdmin, IsSupplier
from common.mixins.custom_api_view import CustomAPIView
from rest_framework.permissions import AllowAny
from common.model_queries import ProductModelQueries


class ProductDeleteView(CustomAPIView, ProductModelQueries):
    """
    Delete a product
    """

    # permission_classes = [IsAdmin]


    def delete(self, request):

        req_validated_data = self.validate_serializer(ProductDetailSerializer, request.data)
        deleted = self.delete_product(req_validated_data["id"])
    
        return Response({
            "data": deleted
        }, status=status.HTTP_200_OK)