from django.db import models
from django.contrib.auth.models import AbstractUser

#抽象クラスAbstractUserを継承してユーザ認証クラスを作成。
class CustomUser(AbstractUser):
    pass




