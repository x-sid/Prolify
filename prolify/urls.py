from django.conf import settings
from django.urls import include,path,re_path
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
from django.conf.urls.static import static

urlpatterns = [
    
    path(r'admin/', admin.site.urls),
    re_path(r'^login/$',LoginView.as_view(),name='login',kwargs={'redirect_authenticated_user': True}),
    re_path(r'^logout/$',LogoutView.as_view(),name='logout', kwargs={'next_page': '/login'}),
    re_path(r'^password-reset/$',PasswordResetView.as_view(),name='password_reset'),
    re_path(r'^password-reset/done/$',PasswordResetDoneView.as_view(),name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    re_path(r'^reset/done/$',PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('',include('album.urls')),
    path(r'',include('album.Api.urls')),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)