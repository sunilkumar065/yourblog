from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from blog.models import Post,Comment

class CommentSerializer(EmbeddedDocumentSerializer):
	class Meta:
		model = Comment
		fields = '__all__'

class PostListSerializer(DocumentSerializer):
	comments = CommentSerializer(many=True)

	class Meta:
		model = Post
		fields = ('title','content','comments')
		depth = 2

class PostCreateSerializer(DocumentSerializer):
	comments = CommentSerializer(many=True)

	class Meta:
		model = Post
		fields = ('title','content','tags','comments')
		depth = 2

	def create(self,validated_data):
		comment = validated_data.pop('comments')
		post = Post.objects.create(**validated_data,comments=comment)
		return post


