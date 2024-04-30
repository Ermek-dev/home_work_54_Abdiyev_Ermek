from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views
from .views.base import index_view
from .views.products import product_detail_view, category_add_view, product_add_view, update_view, confirm_delete, \
    delete_view

urlpatterns = [
    path('', index_view,name='index'),
    path('products/', index_view),
    path('products/<int:pk>',product_detail_view,name='product_detail'),
    path('categories/add',category_add_view, name='category_add'),
    path('products/add/',product_add_view, name='product_add'),
    path('product/<int:pk>/update',update_view,name='product_update'),
    path('product/<int:pk>/delete',delete_view,name='product_delete'),
    path('product/<int:pk>/confirm_delete',confirm_delete,name='confirm_delete'),
    # path('edit/<int:pk>', product_update, name='product_edit'),
    # path('delete/<int:pk>', product_delete, name='product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




    # path('products/add/',product_add_view, name='product_add'),
    # path('products/<int:pk>',detail_view,name='product_detail'),