from django.conf.urls import url

from . import views

app_name = 'manbooks'
urlpatterns = [
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'(?P<pk>[0-9]+)/$', 
        views.DetailView.as_view(), name='detail'),
     url(r'^newbook/$', views.newbook, name='newbook'),
     url(r'^addnew/$', views.addnew, name='addnew'),
     url(r'^(?P<book_id>[0-9]+)/delbook/$', views.delbook, name='delbook'),
]