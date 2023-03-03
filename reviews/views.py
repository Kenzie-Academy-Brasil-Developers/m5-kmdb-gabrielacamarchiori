from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Review
from .serializers import ReviewSerializer
from movies.permissions import IsCritic
from django.shortcuts import get_object_or_404
from movies.models import Movie


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCritic]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        get_object_or_404(Movie, id=self.kwargs.get('movie_id'))
        return serializer.save(movie_id=self.kwargs.get("movie_id"), critic=self.request.user)
