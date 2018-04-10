from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from accounts.serializers import UserSerializer

class Dashboard(APIView):
    def get(self,request,**kwargs):
        pk = kwargs.get('pk')
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'msg':'No user with this id'},status=status.HTTP_204_NO_CONTENT)

class RegistrationView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            dashboard_url = reverse('dashboard',kwargs={'pk':user.id})
            return HttpResponseRedirect(dashboard_url)
        else:
            return Response(serializer.errors)

class LoginView(APIView):
    def post(self,request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        if email and password:
            user = authenticate(request,username=email,password=password)
            if user:
                login(request,user)
                return Response({'logged_in':True})
            else:
                return Response({'user':False})
        else:
            return Reponse({'sucess':False})

def logout_view(request):
    logout(request)
    return HttpResponse('Successfully logged out')
