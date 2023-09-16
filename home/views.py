from audioop import reverse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    return render(request, "index.html")
def index2(request):

    return render(request, "community.html")
def afterlogin(request):
    return render(request,"afterlogin.html")
def therapist(request):
    return render(request, "therapist.html")
def games(request):
    return render(request, "games.html")
def sos(request):
    return render(request, "sos.html")

def ac(request):
    if request.method=='POST':
        context = request.POST.get('comment')
        user = request.user
        if context != '':
            person = Commentac(user=user,context=context)
            person.save()
            redirect('ac')
    
    Comment1 = Commentac.objects.all()
    context = {'Comment1':Comment1}
    return render(request, "ac.html",context)

def dc(request ):
    if request.method=='POST':
        context = request.POST.get('comment')
        user = request.user
        if context != '':
            person = Commentdc(user=user,context=context)
            person.save()
            redirect('dc')

    #Comment1 = Commentdc.objects.all()
    Comment1 = Commentdc.objects.order_by('dates')
    context = {'Comment1':Comment1}
    return render(request, "dc.html",context)

def anger(request):
    if request.method=='POST':
        context = request.POST.get('comment')
        user = request.user
        if context != '':
            person = CommentAI(user=user,context=context)
            person.save()
            redirect('anger')
    
    Comment1 = CommentAI.objects.all()
    context = {'Comment1':Comment1}
    return render(request, "aissues.html",context)






def sos(request):

    if so12.objects.filter(user=request.user) == '':
        return render(request, "sos2.html")
           
    else: 
        if request.method=='POST':
            La = request.POST.get('La')
            Wp = request.POST.get('Fp')
            Sn = request.POST.get('Sn')
            Ws = request.POST.get('Ws')
            Cn = request.POST.get('Ca')
            user = request.user
            try:
                entries = so12.objects.filter(user=request.user)
                entries.delete()
            except:
                pass
            person = so12(user=user,La=La,Fp=Wp,Sn=Sn,Ws=Ws,Ca=Cn)
            person.save()
            return redirect('sos2')
        return render(request, "sos.html") 
        
    
def sos2(request):
    
    SOS1 = so12.objects.filter(user = request.user )
    context = {'sos1':SOS1}
    return render(request, "sos2.html", context)

def Hi(request):
    if request.method=='POST':
        context = request.POST.get('comment')
        user = request.user
        if context != '':
            person = CommentHE(user=user,context=context)
            person.save()
            redirect('Hi')
    
    Comment1 = CommentHE.objects.all()
    context = {'Comment1':Comment1}
    return render(request, "Hi.html",context)

def ri(request):
    if request.method=='POST':
        context = request.POST.get('comment')
        user = request.user
        if context != '':
            person = CommentRE(user=user,context=context)
            person.save()
            redirect('ri')
    
    Comment1 = CommentRE.objects.all()
    context = {'Comment1':Comment1}
    return render(request, "ri.html",context)

def ms(request):
    if request.method=='POST':
        context = request.POST.get('comment')
        user = request.user
        if context != '':
            person = CommentMS(user=user,context=context)
            person.save()
            redirect('ms')
    
    Comment1 = CommentMS.objects.all()
    context = {'Comment1':Comment1}
    return render(request, "ms.html",context)

def login1(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            username = request.POST.get('txt')
            email = request.POST.get('email')
            password = request.POST.get('pswd')
            Cpassword = request.POST.get('Cpswd')
            if password != Cpassword:
                messages.warning(request,"Password Doesn't Match !!!")
                return redirect('login')
            else :
                try:
                    validate_email(email)
                    print("Email is valid")
                except ValidationError:
                    print("Email is invalid")
                my_user = User.objects.create_user(username,email,password)
                my_user.save()
                return redirect('login')

        # Handle login form submission
        elif 'login' in request.POST:
            username1 = request.POST.get('username')
            password1 = request.POST.get('pass')
            print(username1)
            print(password1)
            user = authenticate(request,username=username1,password=password1)
            
            if user is not None:
                login(request,user)
                return redirect('afterlogin')
            else:
                return redirect('login')

    else:
        return render(request, 'login.html')
    
def chartapp(request):
    return render(request, "chartapp/index.html")