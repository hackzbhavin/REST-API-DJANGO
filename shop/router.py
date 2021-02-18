from shopwebapp.viewsets import ProductViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product',ProductViewSet)
router.register('category',CategoryViewSet)