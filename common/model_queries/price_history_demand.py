from common.models import PriceDemandHistory

class PriceDemandHistoryModelQueries:
    
    def get_historical_data(self, product_id):
        history = PriceDemandHistory.objects.filter(product_id=product_id)
        selling_prices = [record.selling_price for record in history]
        demands = [record.demand for record in history]
        return selling_prices, demands
    
    def get_last_recorded_units_sold(self, product):
        last_record = PriceDemandHistory.objects.filter(product=product).order_by("-recorded_at").first()
        return last_record.demand if last_record else 0
    
    def get_price_history(self, product_id):
        return PriceDemandHistory.objects.filter(product_id=product_id).order_by('recorded_at')
