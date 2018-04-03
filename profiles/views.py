from rest_framework.views import APIView
from profiles.forms import LoginForm
from profiles.serializers import LoginSerializer,RegistrationSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout

class LoginView(APIView):
    def post(self,request):
        import ipdb;ipdb.set_trace()
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            profile = authenticate(email=email,password=password)
            if profile:
                login(request,profile)
                return Response({'login':True})
            else:
                return Response({'login':False})

class RegistrationView(APIView):
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)

class LogoutView(APIView):
    pass
