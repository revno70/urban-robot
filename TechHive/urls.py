"""
URL configuration for TechHive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
#from home import views
from home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,),
    path('homepage/',homepage,name='homepage'),
    path('desktop/',desktop),
    path('laptop/',laptop),
    path('monitor/',monitor),
    path('accessories/',accessories),
    path('gadget/',gadget),
    path('component/',component),
    path('gaming/',gaming),
    path('contact/',contact),
    path('hotdeals/',hotdeals),
    path('hotdeal1/',hotdeal1),
    path('hotdeal2/',hotdeal2),
    path('hotdeal3/',hotdeal3),
    path('login/',login,name='login'),
    path('view_logout/',view_logout),
    path('password_change/',password_change_view),
    path('register/',register,name='register'),
    path('header/',header),
    path('footer/',footer),
  # path('login2/',LoginPage,name='login2'),
  # path('home2/',HomePage,name='home2'),
  # path('logout2/',LogoutPage,name='logout2'),
  # path('signup2/',LogoutPage,name='signup2'),
  # path('register2/',register2,name='register2'),
#password_change

]
