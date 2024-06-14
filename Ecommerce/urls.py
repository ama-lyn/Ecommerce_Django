from django.urls import path
from . import views

urlpatterns = [
    path('products_list/', views.product_list, name='product_list')
]
