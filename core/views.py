from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import send_mail
from send_email.settings import EMAIL_HOST_USER
from .models import emailids
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def home(request):
    if request.user.is_authenticated:   
        user=request.user
        mailids=emailids.objects.filter(user=user)
        if request.method=='POST':
            subject=request.POST['subject']
            message=request.POST['message']
            mark="This email is sent through a free email service https://freemailservice.herokuapp.com/"
            message=message+"\n\n\n\n\n\n"+mark
            listof_mail=[]
            for i in mailids: 
                listof_mail.append(i.email) 
            send_mail(subject,message,EMAIL_HOST_USER,listof_mail)
            messages.success(request,'Your messages has been sent successfully')
            print('Message sent successfully')
        return render(request,'core/index.html',{'mails':mailids})
    return render(request,'core/index.html')       
    

def addemail(request):
    if request.method=='POST':
        user=request.user
        email=request.POST['email']
        mailid=emailids(email=email,user=user)
        mailid.save()
        return redirect('/')
 
def delete(request):
    if request.method=='POST':
        id=request.POST['id']
        mailid=emailids.objects.filter(id=id)
        mailid.delete()
        return redirect('/')

def update(request,id):
    mailid=emailids.objects.filter(id=id).first() 
    return render(request,'core/update.html',{'email':mailid,'email_id':id})

def updatemail(request):
    if request.method=='POST':
        id=request.POST['id']
        email=request.POST['email']
        user=request.user
        mail=emailids.objects.get(id=id)
        mail.email=email
        mail.save()
        return redirect('/')
        
#Account section register,login, logout

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.warning(request,'Email has already taken')
                return redirect('/register/')
            elif User.objects.filter(username=username).exists():
                messages.warning(request,'Username has already taken')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.success(request,'Registration successful!')
                return redirect('/')
        else:
            messages.error(request,'password not matched')
            return redirect('/')
    return render(request,'account/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'User not found')
            return redirect('/login/')
    return render(request,'account/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')