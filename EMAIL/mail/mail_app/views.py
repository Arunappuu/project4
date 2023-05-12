from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User



# Create your views here.
def form(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        subject = request.POST.get('subject')
        from_value = request.POST.get('from')
        
        send_mail(subject, msg, from_value, ['niikhiilmr@gmail.com'], fail_silently=False)
        messages.success(request, "success")
    return render(request, "form.html")   

def setsession(request):
    request.session['sname']='Ram'
    return HttpResponse('mail send')
def getsession(request):
    sname= request.session['sname']
    return HttpResponse('welcome' + sname)
def reg(request):
    if request.method =='POST':
        
        uname= request.POST['name']
        email= request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username already taken')
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('reg')
            else:
                user=User.objects.create_user(username=uname,email=email, password=password)
                user.save()
                
        else:
            messages.info(request,'password not match') 
            return redirect('reg')       
        return redirect('/')
       
      
    return render(request, "register.html")