from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import PostListSerializer,PostCreateSerializer
from blog.models import Post,Comment
from rest_framework import status

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