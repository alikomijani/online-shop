
from .models import Comment, Product, Category
from .serializers import CategorySerializer, CommentSerializer,\
    ProductDetailsSerializer, ProductListSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# def get_products(request):
#     results = []
#     for p in Product.objects.all():
#         results.append({
#             "name": p.name,
#             "slug": p.slug,
#             "description": p.description,
#             "price": p.price
#         })
#     response = {"results": results}
#     return JsonResponse(response)


# def get_product_by_slug(request, slug):
#     product = Product.objects.get(slug=slug)
#     dic = {
#         "name": product.name,
#         "slug": product.slug,
#         "description": product.description,
#         "price": product.price
#     }
#     return JsonResponse(dic)


# @csrf_exempt
# @api_view(['POST', "GET"])
# def categories(request):
#     if request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return JsonResponse(serializer.data)
#     else:
#         serializer = CategorySerializer(
#             instance=Category.objects.all(), many=True)
#         return JsonResponse({"results": serializer.data})


# @csrf_exempt
# @api_view(['PUT', "GET", "DELETE"])
# def category(request, slug):
#     obj = get_object_or_404(Category, slug=slug)
#     if request.method == 'PUT':
#         serializer = CategorySerializer(data=request.data, instance=obj)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return JsonResponse(serializer.data)
#     elif request.method == 'GET':
#         serializer = CategorySerializer(
#             instance=obj)
#         return JsonResponse(serializer.data)
#     elif request.method == 'DELETE':
#         obj.delete()
#         return JsonResponse({'message': "object is deleted!"})


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]


class ProductViewSet(ModelViewSet):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'retrieve':
            return ProductDetailsSerializer
        return super().get_serializer_class()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
