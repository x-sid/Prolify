from django.urls import path,re_path
from . import views

app_name='album'

urlpatterns = [

    path('', views.index, name='index'),

    re_path(r'^register/$',views.register, name='register'),

    re_path(r'^userprofile/edit/$',views.edituserprofile, name='edituserprofile'),

    re_path(r'^userprofile/$',views.userprofile, name='userprofile'),

    re_path(r'^change-password/$',views.change_password, name='change_password'),
    
    #album/profile/2/detail
    re_path(r'^profile/(?P<pk>[0-9]+)/detail/$',views.profile_detail, name='profile_detail'),

    re_path(r'^contacts/$', views.contact, name='contact'),

    #/album/profile/add/
    re_path(r'^profile/add/$', views.profile_add, name='profile_add'),

    #/album/profile/2/update
    re_path(r'^profile/(?P<pk>[0-9]+)/edit/$', views.profile_edit, name='profile_edit'),

     #/album/profile/2/delete
    re_path(r'^profile/(?P<pk>[0-9]+)/delete/$', views.profile_delete, name='profile_delete'),

   
 
]
