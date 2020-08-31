from django.conf.urls import url, include
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from posts.views import *

urlpatterns = [
    #url(r'^posts/$', login_required(posts_view), name='posts'),
    url(r'^posts/$', login_required(PostListView.as_view()), name='posts'),
    url(r'^posts/addpost', login_required(PostCreateView.as_view()), name='addpost')
]