from rest_framework.serializers import Serializer,CharField,EmailField
from rest_framework_mongoengine.serializers import DocumentSerializer
from django.core.validators import validate_email
from profiles.models import Profile

class LoginSerializer(Serializer):
    email = EmailField()
    password = CharField(style={'input_type':'password'})

class RegistrationSerializer(DocumentSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
