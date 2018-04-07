from django.db.models import Model,CASCADE,OneToOneField,CharField,TextField
from django.contrib.auth.models import User

class Profile(Model):
    user = OneToOneField(User,on_delete=CASCADE)
    bio = TextField(blank=True)
    profession = CharField(max_length=50,blank=True)

    def __str__(self):
        return self.user.username
