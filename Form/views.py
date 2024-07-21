from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

# Create login.
class Login(View):
    def get(self, request):
        return render(request, 'auth/login.html')
    
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = email).exists():
            user = authenticate(request, username = email, password = password)
            
            if user != None:
                login(request, user)
                return render(request, 'auth/dummy.html')
            else:
                print('invalid credential')
                return redirect('/')
        else:
            print('email doesnt exists')
            return redirect('register')
    
class Register(View):
    def get(self, request):
        return render(request, 'auth/register.html')
    
    def post(self,request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        country_code = request.POST.get('country_code')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        

        if password != confirm_password:
            print('Password not match')
            return redirect('register')
        
        elif User.objects.filter(username =  email).exists():
            print('email already exists')
            return redirect('register')
        else:
            userobj = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username = email,
                email = email,
                password =password
                                )
            
            profile.objects.create(
                user= userobj,
                country_code = country_code,
                phone_number = phone_number
            )
            print('resger successful')
            return redirect('login') 
class Forget_password(View):
    def get(self, request):
        return render(request, 'auth/forgetpassword.html')
    
    def post(self, request):
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = reverse('password_reset_confirm', args=[uid, token])
            reset_url_full = request.build_absolute_uri(reset_url)

            # Display the reset URL on the page instead of sending an email
            messages.info(request, f'Password reset link: {reset_url_full}')
        else:
            messages.error(request, 'No account found with this email address.')

        return render(request, 'auth/forgetpassword.html')


# View to handle password reset confirmation
class PasswordResetConfirmView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            return render(request, 'auth/password_reset_confirm.html', {'uidb64': uidb64, 'token': token})
        else:
            messages.error(request, 'Password reset link is invalid or has expired.')
            return redirect('login')

    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')

            if new_password1 and new_password2 and new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password has been set. You can now log in with the new password.')
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match or are empty.')
        else:
            messages.error(request, 'Password reset link is invalid or has expired.')

        return render(request, 'auth/password_reset_confirm.html', {'uidb64': uidb64, 'token': token})
    