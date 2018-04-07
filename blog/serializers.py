from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from blog.models import Post,Comment,Tag

class CommentSerializer(ModelSerializer):

	class Meta:
		model = Comment
		fields = ('content','likes','created_on')

class PostSerializer(ModelSerializer):
	'''
		this will only show "id" of comments
		comments = PrimaryKeyRelatedField(many=True,queryset=Post.objects.all())
	'''
	comments = CommentSerializer(many=True,required=False)

	class Meta:
		model = Post
		fields = ('title','content','comments','tags')
		depth = 1
