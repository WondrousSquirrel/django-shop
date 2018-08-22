from django.contrib import admin
from django.urls import path

from shop.views import (
    product_list, 
    product_detail,
)

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<str:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<str:slug>/', product_detail, name='product_detail')
]
