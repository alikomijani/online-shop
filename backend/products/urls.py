from .views import CategoryViewSet, CommentViewSet, ProductViewSet
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'products', ProductViewSet)
urlpatterns = router.urls
