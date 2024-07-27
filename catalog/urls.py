from django.urls import path

from catalog.apps import NewappConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = NewappConfig.name
# urlpatterns = [path('', include("catalog.urls", namespace="catalog"))]
urlpatterns = [# path('', render_home, name='home'),
    # path('contacts/', render_contacts, name='contacts'),
    # path('contacts/', contact_page, name='contact_page'),
    path('', ProductListView.as_view(), name='catalog_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name="product_update"),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete"),]
