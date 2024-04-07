from django.shortcuts import render,redirect
from .forms import LogInForm
from django.contrib.auth import authenticate,login

def index(request):
    if request.method=="POST":
        if request.POST.get('login'):
            return redirect('/login')
        else:
            # return redirect('signing.html')
            pass
        return render(request,'index.html')
    else :
        return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def LogInView(request):
    form = LogInForm()
    message=''
    if request.method=="POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username=data['user_name'],password=data['password'])
            print(user)
            if user is not None:
                login(request,user)
                return redirect ('/home')
        message='login failed!'
    return render(request,'login_user_pass.html',context={'form':form,'message':message})