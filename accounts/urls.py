from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/',
        views.SignUpView.as_view(),
        name = 'signup'),

    path('signup_success/',
        views.SignUpSuccessView.as_view(),
        name='signup_success'),


    # ログイン用のテンプレートをレンダリング
    path('login/',
        auth_views.LoginView.as_view(template_name = 'login.html'),
        name = 'login'),

    # ログアウト用のテンプレートをレンダリング
    path('logout/',
        auth_views.LogoutView.as_view(template_name = 'logout.html'),
        name = 'logout'),
    
]