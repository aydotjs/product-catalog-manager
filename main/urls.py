# urls.py
from django.urls import path
from .views import ProductListView, CustomerListView

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path("customers/", CustomerListView.as_view())
]
