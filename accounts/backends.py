from accounts.models import User

class UserBackend:
    def authenticate(self,request,username,password):
        if username and password:
            try:
                user = User.objects.get(email=username)
                if user.password == password:
                    return user
                else:
                    return None
            except User.DoesNotExist:
                return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
