from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ProductsListView, ProductDetailView, ContactCreateView,
                           ProductCreateView, ProductUpdateView, ProductDeleteView,
                           unpublished_product, products_by_category_view, category_list)


app_name = CatalogConfig.name

urlpatterns = [
    path("catalog/", ProductsListView.as_view(), name="home"),
    path("catalog/contacts/", ContactCreateView.as_view(), name="contact_form"),
    path("catalog/product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/product/new/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/product/update/<int:pk>", ProductUpdateView.as_view(), name="product_update"),
    path("catalog/product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("catalog/product/unpublished/<int:pk>/", unpublished_product, name="product-unpublished"),
    path("catalog/<int:category_id>/", products_by_category_view, name="products_by_category"),
    path("catalog/categories/", category_list, name="category_list"),
]
