from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from login.views import AuthentificationView, SignUpView
from django.views.generic import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy('login'), permanent=False)),
    url(r'^login/$', AuthentificationView.as_view(), name='login'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^logout/$', LogoutView.as_view(), name='logout')
]