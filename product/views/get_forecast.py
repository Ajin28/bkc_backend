from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from common.models import Product
from product.serializers import ProductListSerializer, ProductModelSerializer, ProductDetailSerializer
from common.mixins.permission import IsAdminOrSupplier
from common.mixins.custom_api_view import CustomAPIView
from rest_framework.permissions import AllowAny
from common.model_queries import ProductModelQueries, PriceDemandHistoryModelQueries
import numpy as np
from sklearn.linear_model import LinearRegression
from decimal import Decimal
from common.exceptions import RestAPIException




class ProductForecastView(CustomAPIView, ProductModelQueries, PriceDemandHistoryModelQueries):
    """
    Returns forcast of product
    """

    permission_classes = [IsAdminOrSupplier]


    def get(self, request):

        req_validated_data = self.validate_serializer(ProductDetailSerializer, request.data)
        result = self.calculate_demand_and_optimized_price(req_validated_data["id"])
        return Response({
            "data": result
        }, status=status.HTTP_200_OK)
    

  
    def calculate_demand_and_optimized_price(self, product_id):
        
        product = self.get_product_by_id(product_id)
       
        # Retrieve historical data
        selling_prices, historical_demand = self.get_historical_data(product_id)

        # Ensure latest price and units sold are valid
        if product.selling_price is None or product.units_sold is None:
            raise RestAPIException("Missing required product fields: selling_price or units_sold")

        # Check for historical data
        last_recorded_units_sold = self.get_last_recorded_units_sold(product)
        
        # Calculate latest units sold since the last record
        latest_units_sold = max(product.units_sold - last_recorded_units_sold, 0)  # Ensure non-negative

        # Append the latest price and demand if not already included
        selling_prices.append(float(product.selling_price))
        historical_demand.append(latest_units_sold)

        # Handle missing or insufficient historical data
        if not selling_prices or not historical_demand or len(selling_prices) < 2:
          raise RestAPIException("Insufficient historical data for forecasting")


        # Fit the model with historical + latest data
        X = np.array(selling_prices).reshape(-1, 1)
        y = np.array(historical_demand)
        model = LinearRegression()
        model.fit(X, y)

        # Predict demand at the current price
        forecasted_demand = model.predict([[float(product.selling_price)]])[0]

        # Calculate optimized price (example logic)
        elasticity = Decimal('1.5')  # Convert elasticity to Decimal
        optimized_price = round(product.cost_price * (1 + elasticity), 2)
        # Save results in the product model
        updated_product = self.update_foreast(product, optimized_price, forecasted_demand)
        # Return the results
        return {
            "product_id": updated_product.id,
            "product_name": updated_product.name,
            "forecasted_demand": updated_product.demand_forecast,
            "optimized_price": updated_product.optimized_price,
            "forecast_updated_time": updated_product.forecast_updated_at,
        }