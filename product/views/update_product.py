from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from common.models import Product
from common.mixins.permission import IsAdmin, IsSupplier
from common.mixins.custom_api_view import CustomAPIView
from product.serializers import ProductUpdateSerializer, ProductModelSerializer
from common.model_queries import ProductModelQueries

class ProductUpdateView(CustomAPIView, ProductModelQueries):
    """
    Updates a product
    """
    permission_classes = [IsAdmin]
    
   
    def put(self, request):
    
        req_validated_data = self.validate_serializer(ProductUpdateSerializer, request.data)
        product = self.update_product(req_validated_data)
        res_validated_data = self.validate_model_serializer(ProductModelSerializer, req_data=product) 
        return Response({
            "data": res_validated_data
        }, status=status.HTTP_201_CREATED)
      