from django.conf.urls import url
from blog.views import PostListView,PostCreateView,PostDetailView

urlpatterns = [
	url(r'^$',PostListView.as_view(),name='show-all'),
	url(r'^create',PostCreateView.as_view(),name='create-post'),
	url(r'^view_all',PostListView.as_view(),name='view-all'),
	url(r'^view/(?P<pk>\w+)',PostDetailView.as_view(),name='view-post'),
	url(r'^update/(?P<pk>\w+)',PostDetailView.as_view(),name='update-post'),
	url(r'^delete/(?P<pk>\w+)',PostDetailView.as_view(),name='delete-post'),
]
