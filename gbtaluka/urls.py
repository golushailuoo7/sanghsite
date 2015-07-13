from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile_view, name="profile"),
    url(r'^profile/update$', views.update_profile_view, name="update_profile"),
]
