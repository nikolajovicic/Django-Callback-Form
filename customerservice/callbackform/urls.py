from django.urls import path

from . import views

app_name = 'callbackform'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.contact_view, name='index'),
    path('success/', views.sucess_request, name='sucess_request'),
]