from django.urls import path
from . import views


urlpatterns = [
       path('home/', views.home, name='home'),
       path('about/', views.About_Us, name='About'),
       path('contact/', views.Contact_us, name='Contact'),
       
       
]