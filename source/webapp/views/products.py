from django.core.handlers.wsgi import WSGIRequest
from django.forms import ModelForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from webapp.models import Product, Category



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title','description','price','category','created_at','updated_at','image']


    # def product_add_view(request: WSGIRequest):
#     if request.method == 'GET':
#         form = ProductForm()
#         return render(request, 'product_create.html',context={'form': form})
#     #Post
#     form = ProductForm(data=request.POST)
#     print(form.__dict__)
#     if not form.is_valid():
#         return render(request,
#                       'product_create.html',
#                       context={
#                           'form': form
#                       })
#
#     #Success
#     else:
#         product = Product.objects.create(**form.cleaned_data)
#         return redirect('product_detail',pk=product.pk)
#
# #
#
# def product_add_view(request: WSGIRequest):
#     if request.method == 'GET':
#         return render(request,'product_create.html')
#     product_data = {
#         'title': request.POST.get('title'),
#         'description': request.POST.get('description')
#     }
#     product = Product.objects.create(**product_data)
#     return redirect('product_detail',pk=product.pk)


def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=form.instance.pk)
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})




def category_add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request,'category_create.html')
    category_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description')
    }
    category = Category.objects.create(**category_data)
    return redirect('product_detail',pk=category.pk)




def product_detail_view(request,pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,'product.html',context={
        'product': product
    })

#
# def update_view(request,pk):
#     product = get_object_or_404(Product,pk=pk)
#     if request.method == 'POST':
#         product.title = request.POST.get('title')
#         product.description = request.POST.get('description')
#         product.category = request.POST.get('category ')
#         product.price = request.POST.get('price')
#         product.image = request.POST.get('image')
#         product.save()
#         return redirect('product_detail',pk=product.pk)
#     return render(request, 'product_update.html',
#                   context={
#                   'product':product,
#     })


def update_view(request, pk):
    product = get_object_or_404(Product,pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail',pk=product.pk)
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    form = ProductForm(instance=product)
    return render(request,'product_update.html',context={'form':form, 'product': product })



def delete_view(request,pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request,'product_confirm_delete.html',context={
        'product': product
    })


def confirm_delete(request,pk):
    product = get_object_or_404(Product,pk=pk)
    product.delete()
    return redirect('index')


