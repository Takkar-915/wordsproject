from django.urls import path
from . import views

app_name = 'wordsapp'

urlpatterns =[
    path('',views.IndexView.as_view(),name = 'index'),
    path('details/',views.DetailsView.as_view(),name = 'details'),
    path('top/',views.TopView.as_view(), name = 'top'),
    path('post/',views.CreateView.as_view(), name = 'post'),
    path('post_done/',views.PostSuccessView.as_view(), name = 'post_done'),
    path('<int:pk>/update',views.DataUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete',views.DataDeleteView.as_view(), name = 'delete'),

]