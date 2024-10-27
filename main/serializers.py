# serializers.py
from rest_framework import serializers
from .models import Product, Customer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Alternatively, you can specify fields like ['name', 'description', 'price']
class CustomerSerializer (serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"