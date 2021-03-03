from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView

#Mixin
from django.contrib.auth.mixins import LoginRequiredMixin

#models
from App_Shop.models import Product
# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'
