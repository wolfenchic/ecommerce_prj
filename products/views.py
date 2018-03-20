from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

# Create your views here.
def get_product_page(request):
    products = Product.objects.all()
    return render(request, 'product_page.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {'product': product})