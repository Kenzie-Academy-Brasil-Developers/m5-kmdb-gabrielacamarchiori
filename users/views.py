from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer
from .permissions import IsSuperuser
from rest_framework.generics import ListCreateAPIView


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]

    queryset = User.objects.all()
    serializer_class = UserSerializer
