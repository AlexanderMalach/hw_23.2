from django.urls import path, include
from catalog.apps import NewappConfig
from catalog.views import product_list, contacts, product_detail

app_name = NewappConfig.name

urlpatterns = [
    path('', product_list, name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>/', product_detail, name='product_detail'),
]