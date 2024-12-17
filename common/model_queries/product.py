from common.models import Product
from django.db import IntegrityError
from common.exceptions import RestAPIException
from rest_framework import status
from django.core.paginator import Paginator
from django.utils import timezone


class ProductModelQueries:

    def create_product(self, data):
        """
        Create a new product.
        """
        try:
            product = Product.objects.create(**data)
        except IntegrityError as e:
            print(e)
            raise RestAPIException(e, status_code=status.HTTP_400_BAD_REQUEST)
        return product

    
    def get_product_by_id(self, product_id):
        """
        Retrieve a product by its ID.
        """
        try:
            product = Product.objects.get(id=product_id)
            return product
        except Product.DoesNotExist:
            raise RestAPIException("Product not found", status_code=status.HTTP_409_CONFLICT)

    def get_all_products(self, filters, order_by, page, page_size):
        """
        Retrieve all products.
        """
        
        queryset = Product.objects.filter(**filters).order_by(order_by)
        paginator = Paginator(queryset, page_size)
        page_obj = paginator.get_page(page)
        return page_obj, paginator.count, paginator.num_pages
        

    def update_product(self, data):
        """
        Update product fields by its ID.
        """
        try:
            id = data.pop("id")
            print(id)
            product = Product.objects.get(id=id)
            for key, value in data.items():
                setattr(product, key, value)
            product.save()
            return product
        except Product.DoesNotExist:
            raise RestAPIException("Product not found")
        
    def delete_product(self,product_id):
        """
        Delete a product by its ID.
        """
        try:
            product = Product.objects.get(id=product_id)
            product.delete()
            return True
        except Product.DoesNotExist:
            raise RestAPIException("Product not found")


    def update_foreast(self, product, optimized_price, forecasted_demand):
        product.demand_forecast = forecasted_demand
        product.optimized_price = optimized_price
        product.forecast_updated_at = timezone.now()
        product.save()
        return product
    