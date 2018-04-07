from rest_framework.serializers import ModelSerializer
from blog.models import Post,Comment,Tag

class CommentSerializer(ModelSerializer):

	class Meta:
		model = Comment
		fields = ('content','likes','created_on')

class PostSerializer(ModelSerializer):

	class Meta:
		model = Post
		fields = ('title','content','votes')

class PostDetailSerializer(ModelSerializer):
	comments = CommentSerializer(many=True)

	class Meta:
		model = Post
		fields = ('title','content','comments','tags','created_on','last_edited','votes')
		depth = 1
