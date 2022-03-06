from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def HomePage(request):
        return render(request, "register/home.html")
def About(request):
        return render(request, "register/About.html")
def Why_us(request):
        return render(request, "register/Why_us.html")
def CreatePage(request):
        form = RegisterForm()
        if request.method == "POST":
                form = RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        emailname = request.POST.get("first_name")
                        emailid = request.POST.get("email")
                        #print(emailname)
                        template = render_to_string('register/Email_temp.html', {'name':emailname})
                        email = EmailMessage(
                                'PassAdmin',
                                template,
                                settings.EMAIL_HOST_USER,
                                [emailid],
                                )
                        email.fail_silently=False
                        email.send()
                        if email.send():
                                print("Mail Sent")
                        messages.success(request, 'User Profile Created')
                        return redirect('/Addpassword')
                else:
                        errmsg = "Check Your Credentials"
                        return render(request, 'register/signup.html', {"errormsg": errmsg, "Createform": form})
        return render(request, "register/signup.html", {"Createform": form})

def loginpg(request):
        if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        messages.success(request, 'logged in as ' + username)
                        return redirect('/')
                else:
                        messages.error(request, 'Username or Password is Incorrect')
        return render(request, "register/logins.html")
def logoutuser(request):
        logout(request)
        return redirect('/Home')
