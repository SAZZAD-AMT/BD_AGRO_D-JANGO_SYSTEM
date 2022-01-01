from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
  password1 = forms.CharField(
      help_text='Enter Password',
      required=True,
      widget=forms.PasswordInput(
          attrs={'class': 'form-control', 'placeholder': 'Password'}),
  )
  password2 = forms.CharField(
      required=True,
      help_text='Enter Password Again',
      widget=forms.PasswordInput(
          attrs={'class': 'form-control', 'placeholder': 'Password Confirm'}),
  )

  class Meta:
    model = get_user_model()
    fields = ('first_name', 'last_name', 'username', 'address', 'is_expart', 'phone', 'password1', 'password2')
    widgets = {
      'address': forms.Textarea(attrs={'rows':2, 'cols':15}),
    }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name',
        ]

class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False, error_messages={'invalid': "Image files only"}, widget=forms.FileInput)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image'
        ]