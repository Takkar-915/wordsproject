from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from . import forms

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self,form):
        user = form.save()
        self.object = user

        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('accounts:login_success')

class MyLoginSuccessView(TemplateView):
    template_name = 'login_success.html'

class MyLogoutView(LogoutView):
    template_name = 'logout.html'




 