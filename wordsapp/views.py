from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from wordsapp.forms import PostForm
from .models import Category,Post

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

@method_decorator(login_required, name='dispatch')
class TopView(TemplateView):
    template_name = 'top.html'

    model = Post
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.order_by('-posted_at')
    
    

@method_decorator(login_required, name='dispatch')
class CreateView(CreateView):
    form_class = PostForm
    template_name = "post.html"
    success_url = reverse_lazy('wordsapp:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name ='post_success.html'


