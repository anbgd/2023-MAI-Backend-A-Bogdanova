from rest_framework import serializers
from .models import Country, Breed


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class BreedSerializer(serializers.ModelSerializer):
    Countries = CountrySerializer(many=True, read_only=True)

    class Meta:
        model = Breed
        fields = ('id', 'breed_namee', 'countries')