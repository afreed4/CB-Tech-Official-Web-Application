from django.db.models.query import QuerySet
from django.shortcuts import render
import datetime 
import json
from logging import getLogger
from typing import Any, Dict, Union, List

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse, redirect
from django.utils import timezone
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from . forms import AddToCartForm,StripePaymentForm,AddressForm
from . models import Product,Order,OrderItem,Address,Payment,Category,StripePayment

from .utils import get_or_set_order_session
# Create your views here.

logger=getLogger(__name__)

stripe.api_key=settings.STRIPE_SECRET_KEY


class ProductListView(generic.ListView):
    template_name: str = 'cart/product_list.html'
    
    def get_queryset(self):
        qs=Product.objects.all()
        catagory=self.request.GET.get('catagory', None)
        if not catagory:
            return qs
        return qs.filter(
            Q(primary_catagory__name=catagory) |
            Q(secondary_catagories__name=catagory)
        ).distinct()
        
    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context=super(ProductListView, self).get_context_data(**kwargs)
        context.update({'categories':Category.objects.values('name')})
        return context
        
        
class ProductDetailView(generic.FormView):
    template_name:str='cart/product_detail.html'
    form_class=AddToCartForm
    
    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs['slug'])
    
    def get_success_url(self) -> str:
        return reverse("cart:summary")
    
    def get_form_kwargs(self):
        kwargs=super(ProductDetailView, self).get_form_kwargs()
        kwargs["product_id"]=self.get_object().id
        return kwargs
    
    def form_valid(self, form):
        order=get_or_set_order_session(self.request)
        product=self.get_object()
        
        item_filter=order.items.filter(
            product=product,
            colour=form.cleaned_data['colour'],
            size=form.cleaned_data['size'],
        )
        if not item_filter.exists():
            new_item=form.save(commit=False)
            new_item.product=product
            new_item.order=order
            new_item.save()
        else:
            item=item_filter.first()
            item.quantity +=int(form.cleaned_data['quantity'])
            item.save()
            
        return super(ProductDetailView, self).form_valid(form)
    
    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context=super(ProductDetailView, self).get_context_data(**kwargs)
        context['product']=self.get_object()
        return context
    
class CartView(generic.TemplateView):
    template_name: str = "cart/cart.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context=super(CartView, self).get_context_data(**kwargs)
        context["order"]=get_or_set_order_session(self.request)
        return context
    
class IncreaseQuantityView(generic.View):
    @staticmethod
    
    def get(request, *args, **kwargs) -> Union[HttpResponsePermanentRedirect,HttpResponseRedirect]:
        order_item=get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.quantity += 1
        order_item.save(update_fields=['quantity', ])
        return redirect("cart:summary")
    
    
class DecreaseQuantityView(generic.View):
    @staticmethod
    def get(request, *args, **kwargs) -> Union[HttpResponsePermanentRedirect, HttpResponseRedirect]:
        order_item=get_object_or_404(OrderItem, id=kwargs['pk'])
        if order_item.quantity <= 1:
            order_item.delete()
        else:
            order_item.quantity -=1
            order_item.save(update_fields=['quantity', ])
        return redirect("cart:summary")
    
    
class RemoveFromCartView(generic.View):
    @staticmethod
    def get(request, *args, **kwargs)-> Union[HttpResponsePermanentRedirect,HttpResponseRedirect]:
        order_item=get_object_or_404(OrderItem, id=kwargs['pk'])