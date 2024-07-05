
from email.message import EmailMessage
from django.shortcuts import  redirect, render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from website import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from login.models import Login
from signin.models import Signin
from contact.models import Contact
from login.models import Join

def home(request):
    return render(request, 'home.html')

# Add similar views for other sections if needed
def sale(request):
    return render(request, 'sale.html')
def sale1(request):
    return render(request, 'sale1.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def gotosignin(request):
    return render(request,'signin.html')
def indian(request):
    return render(request, 'indian.html')
def all(request):
    return render(request, 'all.html')
def contact(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email1=request.POST.get('email1')
        message=request.POST.get('message')
        data2=Contact(fullname=name,fullemail1=email1,fullmessage=message)
        data2.save()
    
    return render(request, 'contact.html')
    
def signin(request):
    if request.method=="POST":
        uname1=request.POST.get('uname1')
        email=request.POST.get('email')
        psw1=request.POST.get('psw1')
        data1=Signin(username1=uname1,email=email,password1=psw1)
        data1.save()
    
        return render(request, 'home.html')

def login(request):
    
    if request.method=="POST":
        uname=request.POST.get('uname')
        psw=request.POST.get('psw')
        data=Login(username=uname,password=psw)
        data.save()
        
        return render(request, "home.html")

def joinus(request):
    
    if request.method=="POST":
        namej=request.POST.get('namej')
        instaj=request.POST.get('instaj')
        bdatej=request.POST.get('bdatej')
        numberj=request.POST.get('numberj')
        emailj=request.POST.get('emailj')
        data3=Join(Namej=namej,Instaj=instaj,Bdatej=bdatej,Numberj=numberj,Emailj=emailj)
        data3.save()
        
        return HttpResponseRedirect("/aboutus/")
    
    return render(request, 'joinus.html')