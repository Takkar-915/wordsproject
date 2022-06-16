from turtle import title
from unicodedata import category
from django.db import models
from psutil import users
from accounts.models import CustomUser

# Create your models here.

class Category(models.Model):

    title = models.CharField(
        verbose_name='品詞',
        max_length=20)
    
    def __str__(self):
        """オブジェクトをテキストにして返す"""

        return self.title
    

class Post(models.Model):

    user = models.ForeignKey(
        CustomUser,

        verbose_name= 'ユーザー',

        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,

        verbose_name= 'カテゴリ',

        on_delete= models.PROTECT
    )


    question = models.TextField(
        verbose_name= '英単語'
    )
    answer = models.TextField(
        verbose_name= '意味'
    )

    posted_at = models.DateTimeField(
        verbose_name= '登録日時',
        auto_now_add=True
    )

    def __str__(self):
        """オブジェクトをテキストにして返す"""

        return self.question