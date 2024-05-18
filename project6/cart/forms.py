from typing import Any, Mapping
from django import forms 
from django.contrib.auth import get_user_model
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import OrderItem,ColourVariation,Product,SizeVariation,Address

User=get_user_model()

class AddToCartForm(forms.ModelForm):
    quantity=forms.IntegerField(min_value=1)
    size=forms.ModelChoiceField(queryset=SizeVariation.objects.none())
    colour=forms.ModelChoiceField(queryset=ColourVariation.objects.none())
    
    class Meta:
        model=OrderItem
        fields=['quantity','size','colour']
        
    def __init__(self, *args, **kwargs):
        self.product_id=kwargs.pop('product_id')
        product=Product.objects.get(id=self.product_id)
        super().__init__(*args, **kwargs)
        
        self.fields['colour'].queryset=product.available_colours.all()
        self.fields['size'].queryset=product.available_sizes.all()
        
    def clean(self):
        product=Product.objects.get(id=self.product_id)
        quantity=self.cleaned_data['quantity']
        if product.stock < quantity:
            raise forms.ValidationError(f"The maximum quantity is available is {product.stock}")
    
class AddressForm(forms.Form):
    billing_city=forms.CharField(required=False)
    shipping_city=forms.CharField(required=False)
    billing_zip_code=forms.CharField(required=False)
    shipping_zip_code=forms.CharField(required=False)
    
    billing_address_line_1=forms.CharField(required=False)
    billing_address_line_2=forms.CharField(required=False)
    
    shipping_address_line_1=forms.CharField(required=False)
    shipping_address_line_2=forms.CharField(required=False)
    
    selected_shipping_address=forms.ModelChoiceField(queryset=Address.objects.none(),required=False)
    selected_billing_address=forms.ModelChoiceField(queryset=Address.objects.none(),required=False)
    
    def __init__(self, *args, **kwargs):
        user_id=kwargs.pop('user_id')
        super().__init__(*args, **kwargs)
        
        user=User.objects.get(id=user_id)
        
        shipping_address_qs=Address.objects.filter(user=user,address_type=Address.SHIPPING_ADDRESS_TYPE)
        billing_address_qs=Address.objects.filter(user=user, address_type=Address.BILLING_ADDRESS_TYPE)
        
        self.fields['selected_shipping_address'].queryset=shipping_address_qs
        self.fields['billing_address_qs'].queryset=billing_address_qs
        
    def clean(self):
        data=self.changed_data
        
        selected_shipping_address=data.get('selected_shipping_address',None)
        if selected_shipping_address is None:
            if not data.get('shipping_address_line_1',None):
                self.add_error("shipping_address_line_1","Please fill in this field")
                
            if not data.get('shipping_address_line_2',None):
                self.add_error("shipping_address_line_2","Please Fill Out this field")
                
            if not data.get('shipping_zip_code',None):
                self.add_error("shipping_zip_code","Please Fill Out This Field")
                
            if not data.get("shipping_city",None):
                self.add_error("shipping_city",'PleaseFill Out This Field')
                
            if not data.get("billing_city",None):
                self.add_error("billing_city","Please Fill Out This Field")
                
                
class StripePaymentForm(forms.Form):
    selectcard=forms.CharField()
    
    
__all__ =(
    'AddToCartForm',
    'AddressForm',
    'StripePaymentForm'
)