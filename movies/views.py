from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Movie
from .permissions import IsSuperuserOrNo
from .serializers import MovieSerializer
import ipdb


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrNo]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user, genres=self.request.data['genres'])
