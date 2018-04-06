from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import PostSerializer,CommentSerializer
from blog.models import Post,Comment

class IndexView(APIView):
	def get(self,request):
		res = {'running':True}
		return Response(res)

class PostListView(APIView):
	def get(self,request):
		post = Post.objects.all()
		serializers = PostSerializer(post,many=True)
		return Response(serializers.data)

class CommentListView(APIView):
	def get(self,request):
		comments = Comment.objects.all()
		serializers = CommentSerializer(comments,many=True)
		return Response(serializers.data)
