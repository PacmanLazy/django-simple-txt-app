from django.conf.urls import url, include
from django.urls import reverse_lazy
from posts.views import *

urlpatterns = [
    url(r'^posts/$', PostListView.as_view(), name='posts'),
    url(r'^posts/addpost', PostCreateView.as_view(), name='addpost')
]