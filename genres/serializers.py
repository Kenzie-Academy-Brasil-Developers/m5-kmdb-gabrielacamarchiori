from rest_framework import serializers
from .models import Genre


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    
    class Meta:
        model = Genre
        fields = ['id', 'name']
        
