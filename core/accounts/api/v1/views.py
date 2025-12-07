from accounts.models import UserModel
from rest_framework.generics import CreateAPIView
from .serializers import UserModelSerializer

class RegisterView(CreateAPIView):
    """The view of users register process."""

    queryset = UserModel
    serializer_class = UserModelSerializer
