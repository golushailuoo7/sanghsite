from django.conf.urls import include, url
from django.contrib import admin
from . import views as main_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', main_views.index_view, name="main_index"),
    url(r'^signup/$', main_views.signup_view, name="signup"),

    url(r'^accounts/', include('gbtaluka.urls', namespace="gbtaluka")),

    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
