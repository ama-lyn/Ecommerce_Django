from django.shortcuts import render
from .models import Product


# Create your views here.


def product_list(request):
    products = Product.objects.all()
    
    # The context is defined for readability, ... can be added directly in the render function
    context = {
        'products' : products,
    }
    #passing the html file 
    return render(request, 'Ecommerce/product_list.html', context)


def product_details(request):
    pass
 