from django.urls import include,path,re_path
from .views import ContactRudView,ContactList


urlpatterns = [
    path(r'album/api/contacts/',ContactList.as_view(),name='api-contact-list'),
    re_path(r'^album/api/contacts/(?P<pk>\d+)/$',ContactRudView.as_view(),name='contact-rud')
]