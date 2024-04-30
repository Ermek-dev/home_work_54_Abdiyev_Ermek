from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import Product


def index_view(request:WSGIRequest):
    products = Product.objects.exclude(is_deleted=True)
    context = {
        'products' : products
    }
    return render(request,'index.html',context=context)