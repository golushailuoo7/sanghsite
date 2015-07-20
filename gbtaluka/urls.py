from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile_view, name="profile"),
    url(r'^profile/update$', views.update_profile_view, name="update_profile"),
    url(r'^user/(?P<username>.+)/$', views.user_view, name="user"),
    url(r'^addshakha/$', views.add_shakha_view, name="add_shakha"),
    url(r'^editshakha/(?P<shakha_id>\d+)/$', views.edit_shakha_view, name="edit_shakha"),
    url(r'^shakhas/$', views.shakhas_view, name="shakhas"),
    url(r'^shakha/(?P<shakha_id>\d+)/$', views.shakha_view, name="shakha"),
    url(r'^contacts/$', views.contacts_view, name="contacts"),
    url(r'^editresponsibility/(?P<user_id>\d+)/$', views.edit_responsibility_view, name="edit_responsibility"),
]
