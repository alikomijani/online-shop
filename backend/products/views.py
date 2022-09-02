
from .models import Comment, Product, Category
from .serializers import CategorySerializer, CommentSerializer,\
    ProductDetailsSerializer, ProductListSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductViewSet(ModelViewSet):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filterset_fields = ['category']
    def get_serializer_class(self):
        print(self.action)
        if self.action == 'retrieve':
            return ProductDetailsSerializer
        return super().get_serializer_class()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
