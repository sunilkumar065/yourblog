from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from blog.serializers import PostSerializer
from blog.models import Post,Comment,Tag

class IndexView(APIView):
	def get(self,request):
		res = {'running':True}
		return Response(res)

class PostListView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def list(self,request,*args,**kwargs):
		pk = kwargs.get('pk',None)
		if pk:
			try:
				queryset = self.get_queryset().get(pk=pk)
				serializer = PostSerializer(queryset)
				return Response(serializer.data)
			except Post.DoesNotExist:
				raise Http404
		else:
			queryset = self.get_queryset()
			serializer = PostSerializer(queryset,many=True)
			response = {'posts':[]}
			for data in serializer.data:
				to_append = {'title':'','summary':''}
				to_append.update({'title':data['title'],
								  'summary':data['content'][:50]})
				response['posts'].append(to_append)

			return Response(response)


class PostCreateView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def create(self,request,*args,**kwargs):
		tag_data = request.data.get('tags',None)
		if tag_data:
			request.data.pop('tags')
		post = Post.objects.create(**request.data)
		for tag_id in tag_data:
			post.tags.add(Tag.objects.get(pk=tag_id))
		return Response(request.data)

class PostUpdateDeleteView(RetrieveUpdateDestroyAPIView):

	def get_object(self,pk):
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404

	def put(self,request,*args,**kwargs):
		import ipdb; ipdb.set_trace()
		post = self.get_object(kwargs.get('pk'))
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors)
