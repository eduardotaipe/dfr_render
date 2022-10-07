from rest_framework.viewsets import ModelViewSet

from .models import PetModel
from .serializers import PetModelSerializer


class PetModelViewSet(ModelViewSet):

    queryset = PetModel.objects.all()
    serializer_class = PetModelSerializer

