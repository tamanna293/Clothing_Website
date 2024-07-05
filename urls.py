from django.urls import path
from django.contrib import admin
from .views import *
from blog import views

urlpatterns = [
    path('', home, name='home'),
    path('', indian, name='indian'),
        path('indian/', views.indian, name='indian'),  # Example URL pattern for the 'indian' page
    path('about/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),   
    path('joinus', joinus, name='joinus'),    
    path("sale", sale, name="sale"),
    path("sale1", sale1, name="sale1"),
    path("aboutus", aboutus, name="aboutus"),
    path("indian", indian, name="indian"),
    path("contact", contact, name="contact"),
    path("login", login , name="login"),
    path("all", all , name="all"),
    path("signin", signin , name="signin"),
    path("gotosignin", gotosignin , name="gotosignin"),
   

]
