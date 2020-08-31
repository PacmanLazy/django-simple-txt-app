from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from .utility import LOGIN_TEMPLATE, SIGNUP_TEMPLATE, SIGNUP_SUCCESS_URL
from login.forms import UserSignInForm, UserSignUpForm

# Create your views here.
class AuthentificationView(LoginView):
    template_name = LOGIN_TEMPLATE
    form_class = UserSignInForm

class SignUpView(CreateView):
    template_name = SIGNUP_TEMPLATE
    form_class = UserSignUpForm
    success_url = SIGNUP_SUCCESS_URL

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid