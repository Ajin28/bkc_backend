from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from user.serializers import UserRegisterSerializer
from common.mixins import CustomAPIView
from common.model_queries import UserModelQueries
from common.exceptions import RestAPIException

class RegisterAPIView(CustomAPIView, UserModelQueries):
    """
    API to register a new user.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        validated_data = self.validate_serializer(UserRegisterSerializer, request.data) 
        user = self.create_user(**validated_data)
        refresh = RefreshToken.for_user(user)
        refresh['username'] = user.first_name + " " + user.last_name
        refresh['email'] = user.email
        refresh['role'] = user.role.name
        _ = validated_data.pop('password')
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": validated_data,
        }, status=status.HTTP_201_CREATED)


