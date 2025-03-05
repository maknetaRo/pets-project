from rest_framework import viewsets

from .serializers import PetSerializer, AdminPetSerializer
from .models import Pet

class PetViewSet(viewsets.ModelViewSet):

    queryset = Pet.objects.all()
    serializer_class = AdminPetSerializer