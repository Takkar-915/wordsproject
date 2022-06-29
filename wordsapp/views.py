from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from requests import request
from wordsapp.forms import PostForm
from .models import Category,Post
from django.db.models import Q

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class DetailsView(TemplateView):
    template_name = 'details.html'

@method_decorator(login_required, name='dispatch')
class TopView(ListView):
    template_name = 'top.html'

    model = Post
    

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Post.objects.filter(Q(user = self.request.user) , Q(question__icontains=q_word))
            
        else:
            object_list = Post.objects.filter(user = self.request.user).order_by('memory','-posted_at')
            
        return object_list

@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('wordsapp:top')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        
        postdata.user = self.request.user
        
        postdata.save()
        
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DataUpdateView(UpdateView):
    template_name = 'update.html'
    model = Post
    fields = ['category','question','answer','memory']
    success_url = reverse_lazy('wordsapp:top')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        
        postdata.user = self.request.user
        
        postdata.save()
        
        return super().form_valid(form)
 



@method_decorator(login_required, name='dispatch')
class DataDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Post
    success_url = reverse_lazy('wordsapp:top')
