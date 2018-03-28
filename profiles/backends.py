from profiles.models import Profile

class ProfileBackend:
    def authenticate(self,username=None,email=None,password):
        try:
            profile = Profile.objects.get(email=email)

            if profile.password == password:
                return profile
            else:
                return None
        except Profile.DoesNotExist:
            return None

    def get_user(user):
        try:
            return Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            return None
