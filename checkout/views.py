from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm


# Create your views here.
def checkout(request):
    
    order_form = OrderForm()
    payment_form = MakePaymentForm()
    
    return render(request, "checkout/checkout.html",  {'order_form': order_form, 'payment_form': payment_form, 'publishable': 'whatever' })