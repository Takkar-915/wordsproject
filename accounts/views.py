from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView,TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from . import forms

class SignUpView(CreateView):
    #インスタンス化するフォームクラスを指定
    form_class = CustomUserCreationForm

    #レンダリングするテンプレートを指定
    template_name = 'signup.html'

    #リダイレクト先の指定
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self,form):
        #フォームの入力データをデータベースに保存
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