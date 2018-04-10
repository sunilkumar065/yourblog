from django.db.models import EmailField,CharField,BooleanField,TextField
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager

class User(AbstractBaseUser):
    email = EmailField(unique=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    username = CharField(max_length=255,unique=True)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    staff = BooleanField(default=False)
    bio = TextField(blank=True)
    profession = CharField(max_length=255,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def get_full_name(self):
        return "{0} {1}".format(self.first_name,self.last_name)

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()
