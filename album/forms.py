from django.contrib.auth.models import User
from django import forms
from.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegisterUserForm(UserCreationForm):
    email=forms.EmailField(required=True,max_length=250)
    password1=forms.CharField(required=True,label='password',widget=forms.PasswordInput,help_text='')
    password2=forms.CharField(required=True,label='confirm password',widget=forms.PasswordInput,help_text='')
    username=forms.CharField(required=True,help_text='')

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


def save(self,commit=True):
    user=super(RegisterUserForm,self).save(commit=False)
    user.first_name=self.cleaned_data('first_name')
    user.last_name=self.cleaned_data('last_name')
    user.email=self.cleaned_data('email')
    user.password1=self.cleaned_data('password1')
    user.password2=self.cleaned_data('password2')

    if not password1 and not password2 or password1 != password2:
        raise forms.ValidationError("passwords don't match ")
    return self.cleaned_data

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
