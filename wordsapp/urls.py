from django.urls import path
from . import views

app_name = 'wordsapp'

urlpatterns =[
    path('',views.IndexView.as_view(),name = 'index'),
    path('top/',views.TopView.as_view(), name = 'top'),
    path('post/',views.CreateView.as_view(), name = 'post'),
    path('post_done/',views.PostSuccessView.as_view(), name = 'post_done'),

]