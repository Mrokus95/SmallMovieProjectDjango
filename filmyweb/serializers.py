from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Film


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'username', 'email']

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Film
        fields = ['title', 'year', 'type', 'director', 'description', 'release_date', 'imdb_rating', 'poster']