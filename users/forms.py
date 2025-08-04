from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'given_name', 'middle_initial',
            'last_name', 'suffix', 'sex', 'contact_no', 'campus', 'college', 'role',
            'degree', 'expertise', 'company', 'industry', 'is_expert', 'profile_picture',
            'created_by'
        ]

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
