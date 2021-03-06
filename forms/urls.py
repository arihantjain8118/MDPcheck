from django.conf.urls import url ,include
from django.urls import path
from forms import views

urlpatterns = [
     url(r'^$', views.form_view, name='form_view'),
     path('formsubmit/',views.form_submit,name='form_submit'),
     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
     url(r'^director/activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.director_activate, name='director_activate'),

     ]
