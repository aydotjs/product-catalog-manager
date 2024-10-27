from rest_framework import generics  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Customer
from .serializers import ProductSerializer, CustomerSerializer

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()  # Fetch all products from the database
        serializer = ProductSerializer(products, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class CustomerCreate(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
