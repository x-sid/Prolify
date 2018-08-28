
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.urls import include,path,re_path
from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls.static import static

urlpatterns = [
    
    path(r'admin/', admin.site.urls),
    re_path(r'^login/$',views.login,name='login',kwargs={'redirect_authenticated_user': True}),
    re_path(r'^logout/$',views.logout,name='logout', kwargs={'next_page': '/login'}),
    re_path(r'^password-reset/$',views.password_reset,name='password_reset'),
    re_path(r'^password-reset/done/$',views.password_reset_done,name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',views.password_reset_confirm,name='password_reset_confirm'),
    path('',include('album.urls')),
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)