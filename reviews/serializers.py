from rest_framework import serializers
from .models import Review
from users.serializers import UserSerializerCritic


class ReviewSerializer(serializers.ModelSerializer):
    critic = UserSerializerCritic(read_only=True)
    id = serializers.UUIDField(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'stars', 'review', 'spoilers', 'movie_id', 'critic']
        read_only_fields = ['movie_id']
    
        
