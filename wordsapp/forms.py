import pstats
from pyexpat import model
from attr import field
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ['category','question','answer']