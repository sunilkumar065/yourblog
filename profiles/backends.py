from profiles.models import Profile

class ProfileBackend:
    def authenticate(self,email,password):
        try:
            profile = Profile.objects.get(email=email)

            if profile.password == password:
                return profile
            else:
                return None
        except Profile.DoesNotExist:
            return None

    def get_user(self,email):
        try:
            return Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            return None
