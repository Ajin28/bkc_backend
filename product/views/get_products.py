from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from common.models import Product
from product.serializers import ProductListSerializer, ProductModelSerializer
from common.mixins.permission import IsAdmin, IsSupplier
from common.mixins.custom_api_view import CustomAPIView
from rest_framework.permissions import AllowAny
from common.model_queries import ProductModelQueries


class ProductListView(CustomAPIView, ProductModelQueries):
    """
    Returns a list of products
    """

    permission_classes = [AllowAny]


    # Retrieve all products
    def get(self, request):

        req_validated_data = self.validate_serializer(ProductListSerializer, request.data)
        print(req_validated_data)
        filters = {}
        if req_validated_data["category"]: filters["category__icontains"] = req_validated_data["category"]
        if req_validated_data["name"]: filters["name__icontains"] = req_validated_data["name"]

        products, count, pages = self.get_all_products(
            filters,
            order_by = req_validated_data["order_by"],
            page= req_validated_data["page"],
            page_size= req_validated_data["page_size"]
        )

        print(products)
        res_validated_data = self.validate_model_many_serializer(ProductModelSerializer, req_data=products.object_list) 
        return Response({
            "page" : req_validated_data["page"],
            "count": count,
            "page_size": req_validated_data["page_size"],
            "total_pages": pages,
            "data": res_validated_data

        }, status=status.HTTP_200_OK)