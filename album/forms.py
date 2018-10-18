from django.contrib.auth.models import User
from django import forms
from.models import  Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class RegisterUserForm(UserCreationForm):
    username=forms.CharField(required=True,label='username',widget=forms.TextInput(attrs={'placeholder': 'username'}))
    first_name=forms.CharField(required=True,label='First Name',widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name=forms.CharField(required=True,label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email=forms.EmailField(required=True,max_length=250,widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1=forms.CharField(required=True,label='password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(required=True,label='confirm password',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))
    username=forms.CharField(required=True,help_text='')

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']


    def save(self,commit=True):
        user=super(RegisterUserForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email=self.cleaned_data['email']
        user.phone_number=self.cleaned_data['phone_number']
        user.password=self.cleaned_data['password']
        user.set_password(password)

        if password1 and password2 and password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',)

        if commit:
            user.save()


class EditProfileForm(UserChangeForm):
    password=forms.CharField(required=False,help_text='',widget=forms.PasswordInput)
    username=forms.CharField(help_text='')
   
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']

    
class  ProfileForm(forms.ModelForm):
    first_name=forms.CharField(required=True,max_length=10,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name=forms.CharField(required=True,max_length=10,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    country=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    location=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    description=forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder': 'Description'}))
    phone_number=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': '+234 phone number'}))
    


    class Meta:
        model=Profile
        fields=['first_name','last_name','country','location','description','phone_number','photo']
