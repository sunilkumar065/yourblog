from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from accounts.models import User
from blog.models import Post
from blog.serializers import PostSerializer
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
            return Response(serializer.data)
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
                return Response({'success':'True','msg':'logged_in'})
            else:
                return Response({'success':'False','msg':'no such user'})
        else:
            return Response({'success':'False','msg':'no such user'})

def logout_view(request):
    logout(request)
    return HttpResponse('Successfully logged out')

class PostOfUserView(APIView):
    def get(self,request,**kwargs):
        pk = kwargs.get('pk')
        user = User.objects.get(pk=pk)
        post = Post.objects.filter(user=user)
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)
