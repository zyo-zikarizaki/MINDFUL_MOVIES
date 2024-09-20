from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SignupForm(UserCreationForm):
    email = forms.CharField(
        max_length=254, 
        help_text='メールアドレスは任意です',
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'メールアドレスを入力'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'パスワードは8文字以上'}),
        validators=[MinLengthValidator(8)],
        help_text='パスワードは8文字以上である必要があります。'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'パスワードを再入力'}),
        help_text='パスワードを再入力してください。'
    )

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

