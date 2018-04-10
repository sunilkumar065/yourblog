from rest_framework.serializers import ModelSerializer,ValidationError,CharField
from accounts.models import User

class UserSerializer(ModelSerializer):
    password = CharField()
    password2 = CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email','first_name','last_name','username','password','password2','bio','profession')

    def validate(self,obj):
        pass1 = obj['password']
        pass2 = obj['password2']
        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError('Password does not match')
        else:
            return obj

    def create(self,validated_data):
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        return user
