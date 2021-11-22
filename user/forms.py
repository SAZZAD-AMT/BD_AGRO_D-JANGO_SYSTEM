from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


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


