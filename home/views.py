from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from home.models import *
from django.contrib.auth import authenticate,login as auth_login ,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request, 'home/project.html')

def desktop(request):
    return render(request, 'home/1 desktop.html')

def laptop(request):
    return render(request, 'home/2 laptop.html')

def monitor(request):
    return render(request, 'home/3 monitor.html')

def accessories(request):
    return render(request, 'home/4 accessories.html')

def gadget(request):
    return render(request, 'home/5 gadget.html')

def component(request):
    return render(request, 'home/6 component.html')

def gaming(request):
    return render(request, 'home/7 gaming.html')

def contact(request):
    return render(request,'home/contact us.html')

def hotdeals(request):
    return render(request,'home/hot deals.html')

def hotdeal1(request):
    return render(request,'home/hotdeal1.html')

def hotdeal2(request):
    return render(request,'home/hotdeal2.html')

def hotdeal3(request):
    return render(request,'home/hotdeal3.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1) 
        print(user)
        if user is not None:
            print("User found")
            auth_login(request,user)
            return redirect('homepage')
        else:
            
            print("User not found")
            error = 'Email and password not matched!'
            context = {
                'error' : error
            }
            return render(request, 'home/log in.html', context)
        
    return render(request,'home/log in.html')

@login_required(login_url='login')
def view_logout(request):
    logout(request)
    return redirect("login")

def register(request):
     if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('Confirm Password')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email)
            my_user.set_password(pass1)
            my_user.save()
            return redirect('login')
        
     return render(request,'home/Register.html')

def header(request):
    return render(request, 'home/header.html')

def footer(request):
    return render(request, 'home/footer.html')

def password_change_view(request): 
      
     if request.method=='POST': 
         username = request.user.username 
         current_password = request.POST['cpass'] 
         print(type(username)) 
         user = authenticate(username=username,password = current_password) 
  
         if user is not None: 
              
             current_user = User.objects.get(username=username) 
              
             password1 = request.POST['pass1'] 
             password2 = request.POST['pass2'] 
              
              
             if password1 == password2: 
                 current_user.set_password(password1) 
                 current_user.save() 
                 messages.success(request,'Password Changed Successfully')   
             else: 
                 messages.error(request,"New Password and Confirm Password do not match.") 
         else: 
             messages.error(request,"Current Password does not match.") 
          
      
     return render(request, 'home/password_change.html')



def register2(request): 
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phonenumber=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.error(request,'username or email is already Exist')
            return redirect('register')
        else:
            pdUser=User(email=email,first_name=first_name,last_name=last_name,)
            pdUser.set_password(password)
            pdUser.save()
            customer=Customer
    return render(request, 'home/register2.html')


