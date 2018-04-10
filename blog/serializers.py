from rest_framework.serializers import ModelSerializer
from blog.models import Post,Comment,Tag

class TagSerializer(ModelSerializer):

	class Meta:
		model = Tag
		fields = ('id','tag')

class CommentSerializer(ModelSerializer):

	class Meta:
		model = Comment
		fields = ('content','likes','created_on')

class PostSerializer(ModelSerializer):

	class Meta:
		model = Post
		fields = ('id','title','content','votes')

class PostDetailSerializer(ModelSerializer):
	comments = CommentSerializer(many=True)
	tags = TagSerializer(many=True)

	class Meta:
		model = Post
		fields = ('id','title','content','comments','tags','created_on','last_edited','votes')
