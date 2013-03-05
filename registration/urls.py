from django.conf.urls.defaults import *
from registration import views

urlpatterns = patterns('',
 # Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
)