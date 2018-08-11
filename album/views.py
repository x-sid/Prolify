from django.shortcuts import render,get_object_or_404,redirect
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from.forms import ProfileForm,RegisterUserForm,EditProfileForm


def index(request):
    profiles=Profile.objects.all()
    return render(request,'album/index.html',{'profiles':profiles})

def contact(request):
    profiles=Profile.objects.all()
    return render(request,'album/contact_list.html',{'profiles': profiles})

def profile_detail(request,pk):
    contact=get_object_or_404(Profile,pk=pk)
    args={'contact': contact}
    return render(request, 'album/profile_detail.html',args)


def profile_add(request):
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save()
            return redirect('album:profile_detail',pk=profile.pk)
    else:
        form=ProfileForm()
    return render(request,'album/profile_form.html',{'form':form})


def profile_edit(request, pk):
    contact = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES, instance=contact)
        if form.is_valid():
            contact= form.save(commit=True)
            return redirect('album:profile_detail', pk=contact.pk)
    else:
        form = ProfileForm(instance=contact)
    return render(request, 'album/profile_form.html', {'form': form},)   


def profile_delete(request, pk):
    profile = get_object_or_404(Profile, pk=profile.pk)
    profile.delete()
    return redirect('index')


def userprofile(request):
    args={'user':request.user}
    return render(request,'account/userprofile.html',args)

def edituserprofile(request):
    if request.method=='POST':
       form=EditProfileForm(request.POST,instance=request.user)

       if form.is_valid():
            form.save()
            return redirect('album:edituserprofile')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'account/edit_userprofile.html',args)


def change_password(request):
    if request.method=='POST':
       form=PasswordChangeForm(data=request.POST,user=request.user)

       if form.is_valid():
            form.save()
            return redirect('album:userprofile')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'account/change_password.html',args)

def register(request):
    if request.method =='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/userprofile')
    else: 
       form=RegisterUserForm()
       args={'form':form}
       return render(request,'account/registration_form.html',args)       