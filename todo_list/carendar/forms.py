from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='eメールアドレスは必須です')

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

