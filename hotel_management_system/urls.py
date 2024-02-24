from django.urls import path

from . import views

urlpatterns = [
      path("", views.index, name="index"),
      path("Hotel/Signup/",views.hotel_signup, name= "hotel_signup"),
      path("Hotel/Login",views.hotel_login, name = "hotel_login"),
]
