from common.models import Role
from common.exceptions import RestAPIException

class RoleModelQueries:

    def get_role_by_name(self, role):
        try:
            return Role.objects.get(name=role)
        except Role.DoesNotExist:
            raise RestAPIException('Role does not exists')
        except Exception as e:
            print(e)
            raise RestAPIException('Something went wrong')
        

