'''from django.urls import path

from . views import (
    cart_add, 
    cart_detail, 
    cart_remove
)

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart-detail'),
    path('add/<int:product_id>/', cart_add, name='cart-add'),
    path('remove/<int:product_id>/', cart_remove, name='cart-remove'),
]
'''
from django.conf.urls import url
from . import views
 
app_name = 'cart'
 
urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]