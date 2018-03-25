from django.conf.urls import url
from blog.views import PostListView

urlpatterns = [
	url(r'^',PostListView.as_view(),name='show-all'),
]