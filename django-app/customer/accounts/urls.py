from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

path('login',views.login),
path('signup',views.signup),
path("",views.home,name='home'),
]