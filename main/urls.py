# urls.py
from django.urls import path
from .views import ProductListView, CustomerListView, CustomerCreate, ProductCreate

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path("customers/", CustomerListView.as_view()),
    path("customers/create/", CustomerCreate.as_view()),
    path("products/create/", ProductCreate.as_view())
]
