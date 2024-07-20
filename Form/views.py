from django.shortcuts import render, redirect
from django.views import View

# Create login.
class Login(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    
class Register(View):
    def get(self, request):
        return render(request, 'auth/register.html')
    
    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
    
class Forget_password(View):
    def get(self, request):
        return render(request, 'auth/forgetpassword.html')