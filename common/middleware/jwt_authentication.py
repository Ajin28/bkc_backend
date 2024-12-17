import jwt
from django.conf import settings
from django.http import JsonResponse
from common.model_queries import UserModelQueries
from common.models import CustomUser

class JWTAuthenticationMiddleware:
    """
    Middleware to authenticate requests using JWT in the Authorization header,
    with the ability to skip authentication for certain routes.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # Define non-authenticated routes
        self.non_authenticated_routes = [
            '/user/login/',   
            '/user/register/',  
            '/admin/' 
        ]
    

    def __call__(self, request):
        # Skip authentication for non-authenticated routes
        print("here")
        if any(request.path.startswith(route) for route in self.non_authenticated_routes):
            return self.get_response(request)

        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user_id = decoded.get("user_id")
                request.user = UserModelQueries().get_user_by_id(user_id)
                request.token_payload = decoded
                setattr(request, "_dont_enforce_csrf_checks", True)

            except jwt.ExpiredSignatureError:
                return JsonResponse({"detail": "Token has expired."}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({"detail": "Invalid token."}, status=401)
            except CustomUser.DoesNotExist:
                return JsonResponse({"detail": "User not found."}, status=401)
            
            print(request)
        else:
            return JsonResponse({"detail": "Authentication credentials were not provided."}, status=401)

        return self.get_response(request)
