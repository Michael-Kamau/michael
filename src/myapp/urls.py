from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name='myapp'

urlpatterns = [
    
    url(r'^$',views.about,name='about'), 
    url(r'^applications/$',views.applications,name='applications'), 
    url(r'^contacts/$',views.contacts,name='contacts'), 
]

