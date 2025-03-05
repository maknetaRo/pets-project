from rest_framework import serializers
from .models import Pet



class PetSerializer(serializers.ModelSerializer):
    custom_id = serializers.ReadOnlyField()

    class Meta:
        model = Pet 
        fileds = ['custom_id']

class AdminPetSerializer(PetSerializer):

    class Meta:
        model = Pet
        fields = '__all__'
