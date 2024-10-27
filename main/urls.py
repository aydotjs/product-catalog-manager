# urls.py
from django.urls import path
from .views import ProductListView, CustomerListView, CustomerCreate

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path("customers/", CustomerListView.as_view()),
    path("customers/create/", CustomerCreate.as_view())
]
