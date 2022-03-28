from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .passwordform import passer
from .models import *
import pyperclip
# Create your views here.

def handler404(request,exception):
     context = {'imgloc': "{% staticAssets/Images/undraw_page_not_found_re_e9o6.svg%}"}
     return render(request, 'main/404Error.html', context)
@login_required(login_url='Home/')
def home(request):
     passes = passer()
     if request.method == "POST":
          vali = passer(request.POST)
          if vali.is_valid():
               tn = vali.save()
               request.user.Passodata.add(tn)
               messages.success(request, "Your Password was saved")
               #print("data stored")
          else:
               messages.error(request, "Data was not saved, Check the Credentials")
     context= {'pask': passes}
     return render(request,"main/homeindex.html", context)
def About(request):
     return render(request, "main/About.html")
def contact_us(request):
     if request.method == "POST":
          fs_name = request.POST.get("firstname")
          mail = request.POST.get("Email")
          subject = request.POST.get("Subject")
          Message = request.POST.get("Message")
          template = render_to_string('main/Email.html', {'name': fs_name, 'mail': mail, 'sub': subject, 'msg': Message})
          email = EmailMessage(
                              'PassAdmin_Contact_Form',
                              template,
                              settings.EMAIL_HOST_USER,
                              ['magudesh2006@gmail.com'],
                              )
          email.fail_silently=False
          email.send()
          if email.send():
               print("Mail Sent")
     return render(request, "main/contact.html")

@login_required(login_url='HomePage')
def Passwords(request):
     passname = passmanager.objects.all()
     data_count = request.user.Passodata.all()
     return render(request, "main/vault.html", {'data': passname})
def Delete(request,pk):
     delof = passmanager.objects.get(id=pk)
     delof.delete()
     return redirect('/Vault')
def Edit(request, pk_test):
     edit_of = passmanager.objects.get(id=pk_test)
     valie = passer(instance=edit_of)
     if request.method == "POST":
          valie = passer(request.POST, instance=edit_of)
          if valie.is_valid():
               tn = valie.save()
               request.user.Passodata.add(tn)
               messages.success(request, "Your Password was saved")
               print("data stored")
               return redirect('/Vault')
     context = {'pask':valie}
     return render(request, 'main/homeindex.html', context)
def Copy(request, pk_testt):
     copy_of = passmanager.objects.get(id=pk_testt)
     do = copy_of.password
     pyperclip.copy(do)
     #print(do)
     return redirect('/Vault')