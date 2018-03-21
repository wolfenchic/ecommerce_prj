from django.conf.urls import url, include
from .views import add_to_cart, view_cart

urlpatterns = [
    url(r'^add/$', add_to_cart, name='add_to_cart'), 
    url(r'^view/$', view_cart, name='view_cart'),
    ]