from django.shortcuts import render,get_object_or_404,redirect
from .models import Profile
from django.db.models import Q 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from.forms import ProfileForm,RegisterUserForm,EditProfileForm


def home(request):
    template='album/home.html'
    context={"home_page":"active"}
    return render(request,template,context)

@login_required
def album(request):
    profile_list=Profile.objects.filter(user=request.user)
    page=request.GET.get('page',1)
    paginator= Paginator(profile_list,8)
    try:
        profiles=paginator.page(page)
    except PageNotAnInteger:
        profiles=paginator.page(1)
    except EmptyPage:
        profiles=paginator.page(page)

    context={"album_page":"active",'profiles':profiles}
    return render(request,'album/album.html',context)


@login_required
def contact(request):
    profile_list=Profile.objects.filter(user=request.user)
    context={"contact_page":"active",'profile_list': profile_list}
    return render(request,'album/contact_list.html',context)


@login_required
def profile_detail(request,pk):
    profile=get_object_or_404(Profile,pk=pk)
    args={'profile': profile}
    return render(request, 'album/profile_detail.html',args)


@login_required
def profile_add(request,pk=None):
    if request.method =='POST':
        form=ProfileForm(request.POST,request.FILES)
        user=request.user
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
            return redirect('album:profile_detail',pk=profile.pk)
    else:
        form=ProfileForm()
        context={'form':form,"profile_add_page":"active"}
    return render(request,'album/profile_form.html',context)


@login_required
def profile_edit(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            profile= form.save(commit=True)
            return redirect('album:profile_detail', pk=profile.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'album/profile_form.html', {'form': form},)   


@login_required
def profile_delete(request, pk):
    profile = get_object_or_404(Profile,pk=pk)
    profile.delete()
    return redirect('album:album')


@login_required
def userprofile(request):
    args={'user':request.user,"userprofile_page":"active"}
    return render(request,'account/userprofile.html',args)


@login_required
def edituserprofile(request):
    if request.method=='POST':
       form=EditProfileForm(request.POST,instance=request.user)
       if form.is_valid():
            form.save()
            return redirect('album:userprofile')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'account/edit_userprofile.html',args)


@login_required
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('album:userprofile')
        else:
            form=PasswordChangeForm(data=request.POST,user=request.user)
            args={'form':form}
            return render(request,'account/change_password.html',args)
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'account/change_password.html',args)


def register(request):
    if request.method =='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album:success')
        else: 
           form=RegisterUserForm(request.POST)
           args={'form':form,"register_page":"active"}
           return render(request,'account/registration_form.html',args)    
    else: 
       form=RegisterUserForm()
       args={'form':form,"register_page":"active"}
       return render(request,'account/registration_form.html',args)       

def success(request):
    return render(request,'account/success.html')


@login_required
def search(request):
    query= request.GET.get('q')
    template='album/search.html'
    lookups=Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(location__icontains=query)|Q(phone_number__icontains=query)|Q(pk__icontains=query)
    results=Profile.objects.filter(lookups,user=request.user).distinct()
    context= {'results':results}
    return render(request,template,context)
