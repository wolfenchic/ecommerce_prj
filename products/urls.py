from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', get_product_page, name='products'), 
    url(r'^(\d+)', product_detail, name='product_detail'),
]