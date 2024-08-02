from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    BlogListView,
    BlogDeleteView,
    BlogUpdateView,
    BlogCreateView,
    BlogDetailView,
)

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="catalog_list"),
    path(
        "products/<int:pk>/",
        cache_page(60)(ProductDetailView.as_view()),
        name="product_detail",
    ),
    path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create/", BlogCreateView.as_view(), name="blog_create"),
    path(
        "blog/<int:pk>/<slug:slug>/update/",
        BlogUpdateView.as_view(),
        name="blog_update",
    ),
    path(
        "blog/<int:pk>/<slug:slug>/delete/",
        BlogDeleteView.as_view(),
        name="blog_delete",
    ),
]
