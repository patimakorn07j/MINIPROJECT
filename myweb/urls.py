"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
from myapp import views

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('contactus/', contactus, name='contactus'),
    path('login/', login, name='login'),
    path('restaurant1/', restaurant1, name='restaurant1'),
    path('restaurant2/', restaurant2, name='restaurant2'),
    path('restaurant3/', restaurant3, name='restaurant3'),
    path('restaurant4/', restaurant4, name='restaurant4'),
    path('restaurant5/', restaurant5, name='restaurant5'),
    path('restaurant6/', restaurant6, name='restaurant6'),
    path('restaurant7/', restaurant7, name='restaurant7'),
    path('restaurant8/', restaurant8, name='restaurant8'),
    path('restaurant9/', restaurant9, name='restaurant9'),
    path('restaurant10/', restaurant10, name='restaurant10'),
    path('allrestaurants/', allrestaurants, name='allrestaurants'),
    path('signup/', signup, name='signup'),
    path('addUser',addUser),
    path('loginForm',loginForm),
    path('logout',logout),
    path('submit_comment',submit_comment),
    path('comment/delete/<int:comment_id>/', delete_comment, name='delete_comment'),

]
