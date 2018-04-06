from django.conf.urls import url
from blog.views import IndexView,PostListView,CommentListView

urlpatterns = [
    url(r'^$',IndexView.as_view(),name='index'),
    url(r'^view',CommentListView.as_view(),name='view-all')
]
