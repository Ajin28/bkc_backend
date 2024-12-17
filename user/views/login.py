from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate
from user.serializers import UserLoginSerializer, UserRegisterSerializer
from common.mixins import CustomAPIView
from common.model_queries import UserModelQueries
from common.exceptions import RestAPIException

class LoginAPIView(CustomAPIView, UserModelQueries):
    """
    API to log in a user and return JWT tokens.
    """
    permission_classes = [AllowAny]

    def post(self, request):

        validated_data = self.validate_serializer(UserLoginSerializer, request.data)       
        user = authenticate(request, email=validated_data["email"], password=validated_data["password"])
        if not user:
            raise RestAPIException("Invalid Credentials", status_code=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        refresh['username'] = user.first_name + " " + user.last_name
        refresh['email'] = user.email
        refresh['role'] = user.role.name
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "role": user.role.name
            }
        }, status=status.HTTP_200_OK)
