from django.contrib.auth.models import User
from django import forms
from.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegisterUserForm(UserCreationForm):
    email=forms.EmailField(required=True,max_length=250)
    password1=forms.CharField(widget=forms.PasswordInput,help_text='')
    password2=forms.CharField(widget=forms.PasswordInput,help_text='')
    username=forms.CharField(help_text='')

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


def save(self,commit=True):
    user=super(RegisterUserForm,self).save(commit=False)
    user.first_name=self.cleaned_data['first_name']
    user.last_name=self.cleaned_data['last_name']
    user.email=self.cleaned_data['email']

    if commit:
        user.save()


class EditProfileForm(UserChangeForm):

    class Meta:
        model=User
        fields=['first_name','last_name','email','password',]

    
class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        fields=['full_name','nationality','location','description','phone_number','photo']
