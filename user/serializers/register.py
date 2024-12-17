from rest_framework import serializers


class UserRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30, required=False, default="")
    role =  serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

    
