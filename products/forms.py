from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name','supplier_name','product_code','quantity','stock_alert','added_date','purchase_date','exp_date','purchase_price','total_price','total_price_with_vat','GC_number','product_details','branch','product_category']