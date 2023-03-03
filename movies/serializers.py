from rest_framework import serializers
from .models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'premiere', 'genres', 'duration', 'overview', 'budget']
    
    def create(self, validated_data: dict) -> Movie:
        genre_separator = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)

        for g in genre_separator:
            g_name = Genre.objects.filter(name__iexact=g['name']).first()
            if not g_name:
                g_name = Genre.objects.create(**g)
            movie.genres.add(g_name)
        return movie
