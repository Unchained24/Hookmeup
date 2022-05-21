from django.urls import path,include
from placeholder import views

urlpatterns = [
    


    path('',views.home, name="home"),
    path('rules/',views.rules, name="rules"),
]