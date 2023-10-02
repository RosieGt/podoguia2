from rest_framework.serializers import ModelSerializer
from .models import Podologo




class PodologoSerializer(ModelSerializer):
    class Meta:
        model = Podologo
        fields = '__all__'
        
      