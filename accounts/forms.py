# UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import forms as auth_forms


from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        
        model = CustomUser
        
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(CustomUserCreationForm):

    def __init__(self,*args, **kw) :
        super().__init__(*args, **kw)
        for field in self.fields.values():
             field.widget.attrs['placeholder'] = field.label
