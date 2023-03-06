from django.urls import include, path
from rest_framework import routers
from .views import AccountViewSet

router = routers.DefaultRouter()
router.register(r'accounts/', AccountViewSet, basename='accounts')

urlpatterns = [
    path('', include(router.urls))
]
