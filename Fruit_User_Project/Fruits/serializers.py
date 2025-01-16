from .models import Fruit
from rest_framework import serializers

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = ['name','cost']