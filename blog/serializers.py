from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from blog.models import Post,Comment,Tag

class TagSerializer(ModelSerializer):
	class Meta:
		model = Tag
		fields = '__all__'

class CommentSerializer(ModelSerializer):

	class Meta:
		model = Comment
		fields = '__all__'

class PostSerializer(ModelSerializer):
	comments = PrimaryKeyRelatedField(many=True,queryset=Post.objects.all())
	tags = PrimaryKeyRelatedField(many=True,read_only=True)

	class Meta:
		model = Post
		fields = ('title','content','comments','tags')
