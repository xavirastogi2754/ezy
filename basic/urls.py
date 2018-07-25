from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^home', views.hello),
    url(r'^form', views.pageForm),
    url(r'^edit', views.editable),
    # url(r'^display', views.hello2),
    url(r'^view', views.viewx),
    url(r'^user/(?P<form_id>\d+)/', views.userprofile),
    url(r'^editUser/(?P<form_id>\d+)/', views.editUser),
    # url(r'^search/', views.formPath),
    # url(r'^form/', views.formDisplay),
]
