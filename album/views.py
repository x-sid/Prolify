from django.shortcuts import render,get_object_or_404,redirect
from .models import Contact
from django.db.models import Q 
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,update_session_auth_hash
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from.forms import ContactForm,RegisterUserForm,EditProfileForm


def home(request):
    template='album/home.html'
    context={"home_page":"active"}
    return render(request,template,context)

@login_required
def album(request):
    contact_list=Contact.objects.filter(user=request.user).order_by('created')
    page=request.GET.get('page',1)
    paginator= Paginator(contact_list,8)
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        contacts=paginator.page(1)
    except EmptyPage:
        contacts=paginator.page(page)

    context={"album_page":"active",'contacts':contacts}
    return render(request,'album/album.html',context)

# view that renders the total number of contact
@login_required
def contact(request):
    contact_list=Contact.objects.filter(user=request.user)
    context={"contact_page":"active",'contact_list': contact_list}
    return render(request,'album/contact_list.html',context)

# view that adds contact 
@login_required
def contact_add(request):
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user=request.user
            contact.save()
            return redirect('album:album')
    else:
        form = ContactForm()
    return render(request,'album/contact_form.html',{"form":form})


# view that show contact details 
@login_required
def contact_detail(request,pk):
    contact=get_object_or_404(Contact,pk=pk)
    args={'contact': contact}
    return render(request, 'album/contact_detail.html',args)


#view that edit's contact
@login_required
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST,request.FILES, instance=contact)
        if form.is_valid():
            contact= form.save(commit=True)
            return redirect('album:contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'album/contact_form.html', {'form': form},)   

# view that delete's contact
@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact,pk=pk)
    data=dict()
    if request.method=='POST':
        contact.delete()
        data['form_is_valid'] = True
        contacts=Contact.objects.filter(user=request.user)
        data['html_contact_list'] = render_to_string('album/partial-album.html', {'contacts':contacts})
    else:
        data['form_is_valid'] = False
        context={'contact':contact}
        data['html_form'] = render_to_string('album/partial-contact-delete.html',context,request=request)
    return JsonResponse(data)


#views that has to do with user's profile
@login_required
def userprofile(request):
    args={'user':request.user,"userprofile_page":"active"}
    return render(request,'account/userprofile.html',args)


@login_required
def edituserprofile(request):
    if request.method=='POST':
       form=EditContactForm(request.POST,instance=request.user)
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

# user signup view
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

# view that searchs for contact(s) from the contact album
@login_required
def search(request):
    query= request.GET.get('q')
    template='album/search.html'
    lookups=Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(location__icontains=query)|Q(phone_number__icontains=query)|Q(pk__icontains=query)
    results=Contact.objects.filter(lookups,user=request.user).distinct()
    context= {'results':results}
    return render(request,template,context)
