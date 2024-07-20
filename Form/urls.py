from django.urls import path
from .views import *

urlpatterns = [
    path('',Login.as_view(), name="login"),
    path('register',Register.as_view(), name="register"),
    path('login/forgetpassword',Forget_password.as_view(), name="forgetpassword"),
]
