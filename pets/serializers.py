from .models import PetModel

from rest_framework.serializers import ModelSerializer


class PetModelSerializer(ModelSerializer):

    class Meta:
        model = PetModel
        fields = '__all__'
