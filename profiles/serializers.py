from rest_framework.serializers import Serializer,CharField
from rest_framework_mongoengine.serializers import DocumentSerializer
from django.core.validators import validate_email
from profiles.models import Profile

class LoginSerializer(Serializer):
    user = CharField(max_length=100)
    password = CharField(style={'input_type':'password'})

class RegistrationSerializer(DocumentSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
