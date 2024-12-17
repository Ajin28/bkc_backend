from common.models import CustomUser
from common.model_queries import RoleModelQueries
from django.db import IntegrityError
from common.exceptions import RestAPIException
from rest_framework import status


class UserModelQueries:

    def create_user(self, email, password, role, **extra_fields):
        role = RoleModelQueries().get_role_by_name(role)
        try:
            user = CustomUser.objects.create_user(email, password, role_id = role.id, **extra_fields)
        except IntegrityError as e:
            raise RestAPIException(e, status_code=status.HTTP_400_BAD_REQUEST)

        return user

    def create_super_user(self, email, password, role):
        role = RoleModelQueries().get_role_by_name(role)
        user = CustomUser.objects.create_user(email, password, role_id = role.id)
        return user


    def get_user_by_id(self, user_id):
        user = CustomUser.objects.get(id = user_id)
        return user
        
