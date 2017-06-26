from django.contrib.auth.models import BaseUserManager
from apps.myuser.models import MyUser as User


class UsernameOrEmailBackend(object):

    def authenticate(self, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        try:
            if email:
                user = User.objects.get(
                    email=BaseUserManager.normalize_email(email)
                )
            else:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    # Only to access the admin.
                    user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
