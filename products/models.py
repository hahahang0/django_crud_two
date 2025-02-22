from django.db import models

# Create your models here.

class Products(models.Model):
    product_id = models.AutoField(primary_key = True)
    product_category = models.IntegerField()
    product_name = models.CharField(max_length=200)
    supplier_name = models.CharField(max_length = 200)
    branch = models.IntegerField()
    product_code = models.CharField(max_length=20)
    quantity = models.IntegerField()
    stock_alert = models.IntegerField()
    added_date = models.DateTimeField()
    purchase_date = models.DateTimeField()
    exp_date = models.DateTimeField()
    purchase_price = models.FloatField()
    total_price = models.FloatField()
    total_price_with_vat = models.FloatField()
    GC_number = models.CharField(max_length=50)
    product_details = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    
    # created_at = models.DateTimeField()

    def __str__(self):
        return self.product_name
