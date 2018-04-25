from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from blog.models import Post,Comment,Tag
from accounts.models import User

class TagSerializer(ModelSerializer):

	class Meta:
		model = Tag
		fields = ('id','tag')

class CommentSerializer(ModelSerializer):

	class Meta:
		model = Comment
		fields = ('content','likes','created_on','user')

class PostSerializer(ModelSerializer):

	class Meta:
		model = Post
		fields = ('id','title','content','votes','user')

class PostDetailSerializer(ModelSerializer):
	comments = CommentSerializer(many=True)
	tags = TagSerializer(many=True)

	class Meta:
		model = Post
		fields = ('id','title','content','comments','tags','created_on','last_edited','votes','user')
