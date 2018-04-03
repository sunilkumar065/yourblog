from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import PostCreateSerializer,PostListSerializer
from blog.models import Post,Comment
from rest_framework import status
from django.http import Http404

class PostListView(APIView):
	def get(self,request):
		posts = Post.objects.all()
		serializer = PostListSerializer(posts,many=True)
		return Response(serializer.data)

class PostCreateView(APIView):
	def post(self,request):
		posts = request.data
		serializer = PostCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
	def get_object(self,pk):
		try:
			post = Post.objects.get(pk=pk)
			return post
		except Post.DoesNotExist:
			raise Http404

	def get(self,request,*args,**kwargs):
		pk = kwargs.get('pk')
		post = self.get_object(pk)
		serializer = PostSerializer(post)
		return Response(serializer.data,)

	def put(self,request,*args,**kwargs):
		pk = kwargs.get('pk')
		post = self.get_object(pk)
		serializer = PostCreateSerializer(post,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Reponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self,request,*args,**kwargs):
		pk = kwargs.get('pk')
		post = self.get_object(pk)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
