from django.urls import path
from .views import index, contact, product, product_list

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product'),
    path('products/', product_list, name='product_list')
]
