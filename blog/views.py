from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import PostListSerializer
from blog.models import Post,Comment

class PostListView(APIView):
	def get(self,request):
		posts = Post.objects.all()
		serializer = PostListSerializer(posts,many=True)
		return Response(serializer.data)