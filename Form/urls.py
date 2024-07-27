from django.urls import path
from .views import *

urlpatterns = [
    path('',Login.as_view(), name="login"),
    path('register',Register.as_view(), name="register"),
    path('login/forgetpassword',Forget_password.as_view(), name="forgetpassword"),
    path('reset-password-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('addprofile', AddProfileView.as_view(), name='addprofile'),
    path('addskill', AddSkillView.as_view(), name='addskill'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('index', Index.as_view(), name='index'),
]
