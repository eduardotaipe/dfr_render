from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PetModelViewSet

router = DefaultRouter()
router.register('pet', PetModelViewSet, basename='pet')


urlpatterns = [
    path('', include(router.urls)),
]
