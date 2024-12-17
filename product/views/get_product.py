from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from common.models import Product
from product.serializers import ProductListSerializer, ProductModelSerializer, ProductDetailSerializer
from common.mixins.permission import IsAdmin, IsSupplier
from common.mixins.custom_api_view import CustomAPIView
from rest_framework.permissions import AllowAny
from common.model_queries import ProductModelQueries


class ProductDetailView(CustomAPIView, ProductModelQueries):
    """
    Returns a list of products
    """

    permission_classes = [AllowAny]


    # Retrieve all products
    def get(self, request):

        req_validated_data = self.validate_serializer(ProductDetailSerializer, request.data)
        product = self.get_product_by_id(req_validated_data["id"])
       
        res_validated_data = self.validate_model_serializer(ProductModelSerializer, req_data=product) 
        return Response({
            "data": res_validated_data
        }, status=status.HTTP_200_OK)