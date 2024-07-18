from django.urls import path
from . import views
urlpatterns = [
   path('',views.Home,name="home"),
   path('login/', views.LoginPage, name="login"),
   path('logout/', views.logoutUser, name="logout"),
   path('register/', views.registerPage, name="register"),



]
