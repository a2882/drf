from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

class productviewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # default
    # this viewset is similar to view.py -> product_list_view and for me view.py is better then viewsets.py
