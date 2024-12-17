from django.db import models
from django.utils.translation import gettext_lazy as _

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    stock_available = models.IntegerField()
    units_sold = models.IntegerField(default=0)
    last_recorded_units_sold = models.IntegerField(default=0)  
    customer_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    demand_forecast = models.IntegerField(default=None, blank=True)
    optimized_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    forecast_updated_at = models.DateTimeField(null=True, blank=True, default=None)  # New field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        # If updating an existing product, check for price changes
        if self.pk:  # Product exists in the database
            old_product = Product.objects.get(pk=self.pk)
            if old_product.selling_price != self.selling_price:
                # Calculate units sold at the old price
                units_sold_since_last_record = self.units_sold - self.last_recorded_units_sold

                # Record price-demand history for the old price
                PriceDemandHistory.objects.create(
                    product=self,
                    selling_price=old_product.selling_price,
                    demand=units_sold_since_last_record
                )

                # Update last recorded units sold
                self.last_recorded_units_sold = self.units_sold

        super().save(*args, **kwargs)


class PriceDemandHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    demand = models.IntegerField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Product: {self.product.name}, Price: {self.selling_price}, Demand: {self.demand}"

