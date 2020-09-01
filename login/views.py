from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from .utility import SIGNIN_TEMPLATE, SIGNUP_TEMPLATE, SIGNUP_SUCCESS_URL, SIGNIN_TITLE, SIGNUP_TITLE
from login.forms import UserSignInForm, UserSignUpForm

# Create your views here.
class AuthentificationView(LoginView):
    template_name = SIGNIN_TEMPLATE
    form_class = UserSignInForm

    def get_context_data(self, *args, **kwargs):
        context = super(AuthentificationView, self).get_context_data(*args, **kwargs)
        context['title'] = SIGNIN_TITLE
        return context

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

    def get_context_data(self, *args, **kwargs):
        context = super(SignUpView, self).get_context_data(*args, **kwargs)
        context['title'] = SIGNUP_TITLE
        return context