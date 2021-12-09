from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, SpecialiteViewSet, RestoViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('specialites', SpecialiteViewSet)
router.register('restos', RestoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]