from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
                # Determine the redirect page after login based on profile and skills
                profile_exists = Profile.objects.filter(user=user).exists()
                skills_exist = Skill.objects.filter(user=user).exists()

                if not profile_exists:
                    return redirect('addprofile')
                elif profile_exists and not skills_exist:
                    return redirect('skills')
                else:
                    return redirect('index') 
        else:
            print('email doesnt exists')
            return redirect('register')

#Create register 
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
            
            Profile.objects.create(
                user= userobj,
                country_code = country_code,
                phone_number = phone_number
            )
            print('resger successful')
            return redirect('login') 


#Create forget password 
class Forget_password(View):
    def get(self, request):
        return render(request, 'auth/forgetpassword.html')
    
    def post(self, request):
        email = request.POST.get('email')
        if not User.objects.filter(email=email).exists():
            print('email does not exist')
            return redirect('forgetpassword')

        user = User.objects.get(email=email)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Create password reset URL
        reset_url = request.build_absolute_uri(f'/reset-password-confirm/{uid}/{token}/')

        # Render email template
        email_subject = 'Password Reset Requested'
        email_body = render_to_string('auth/password_reset_email.html', {
            'user': user,
            'reset_url': reset_url,
        })

        # Send email
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        print('email sent')
        return redirect('login')


#Create password reset  
class PasswordResetConfirmView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            return render(request, 'auth/password_reset_confirm.html', {'user': user})
        else:
            return render(request, 'auth/password_reset_confirm.html', {'invalid': True})

    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                print('Passwords do not match')
                return render(request, 'auth/password_reset_confirm.html', {'user': user, 'error': 'Passwords do not match'})
            
            user.set_password(password)
            user.save()
            print('Password has been reset successfully')
            return redirect('login')
        else:
            return render(request, 'auth/password_reset_confirm.html', {'invalid': True})


#Create profile 
@method_decorator(login_required, name='dispatch')
class AddProfileView(View):
    def get(self, request):
        user=request.user
        # Fetch the profile of the currently logged-in user
        profile, created = Profile.objects.get_or_create(user=user)
        context = {
            'profile': profile
        }
        return render(request, 'auth/profile.html', context)

    def post(self, request):
        user=request.user
        # Fetch the profile of the currently logged-in user
        profile, created = Profile.objects.get_or_create(user=user)
        
        profile_image = request.FILES.get('profile_image')
        timeline_image = request.FILES.get('timeline_image')
        profession = request.POST.get('profession')
        thread_url = request.POST.get('thread_url')
        facebook_url = request.POST.get('facebook_url')
        instagram_url = request.POST.get('instagram_url')
        skype_url = request.POST.get('skype_url')
        linkedin_url = request.POST.get('linkedin_url')
        bio = request.POST.get('bio')
        dob = request.POST.get('dob')
        website = request.POST.get('website')
        degree = request.POST.get('degree')
        country_code = request.POST.get('country_code')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        freelance = request.POST.get('freelance')
        happy_client = request.POST.get('happy_client')
        projects = request.POST.get('projects')
        hr_of_support = request.POST.get('hr_of_support')
        hard_work = request.POST.get('hard_work')
        i_agree = request.POST.get('i_agree') == 'True'

        profile= Profile.objects.get(user=user)
        profile.profile_image = profile_image
        profile.timeline_image = timeline_image
        profile.profession = profession
        profile.thread_url = thread_url
        profile.facebook_url = facebook_url
        profile.instagram_url = instagram_url
        profile.skype_url = skype_url
        profile.linkdin_url = linkedin_url
        profile.bio = bio
        profile.dob = dob
        profile.website = website
        profile.degree = degree
        profile.country_code = country_code
        profile.phone_number = phone_number
        profile.address = address
        profile.freelance = freelance
        profile.happy_client = happy_client
        profile.projects = projects
        profile.hr_of_support = hr_of_support
        profile.hard_work = hard_work
        profile.i_agree = i_agree
        profile.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('addskill')

#Create skill 
class AddSkillView(View):
    def get(self, request):
        skills = Skill.objects.all()
        context = {'skills': skills}
        return render(request, 'auth/skill.html', context)
    
    def post(self,request):
        skill_name = request.POST.get('skill_name')
        skill_percentage = request.POST.get('skill_percentage')

        if skill_name and skill_percentage:
            skill = Skill(user=request.user, skill_name=skill_name, skill_percentage=skill_percentage)
            skill.save()
            messages.success(request,'Skill added successfully.')
            return redirect('index') #temerery
        else:
            messages.error(request, 'Error adding skill. Please fill in all fields.')
        return redirect('addskill')
    
#Create logout 
class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')
    
#create index get for porfolio index
class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            profiles = Profile.objects.get(user = user)
            skills = Skill.objects.filter(user = user)
            context = {'profile': profiles, 'skill':skills}
        else:
            return redirect('login')
        return render(request, 'portfolio/index.html', context)

