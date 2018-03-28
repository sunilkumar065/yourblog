from rest_framework.views import APIView
from profiles.forms import LoginForm
from profiles.serializers import LoginSerializer,RegistrationSerializer
from rest_framework.response import Response

class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.data.get('user')
            password = serializer.data.get('password')

        return Response({'success':True,'user':user})

class RegistrationView(APIView):
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class LogooutView(APIView):
    pass
