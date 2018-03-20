from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.
def get_product_page(request):
    products = Product.objects.all()
    return render(request, 'product_page.html', {'products': products})