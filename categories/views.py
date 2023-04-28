from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer