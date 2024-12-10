
# Create your views here.
from django.shortcuts import render,redirect
from .models  import product,menu,serv,about,cont,projectss,Us,flag
# Create your views here.

def index(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_text = request.POST.get('text')
        cont.objects.create(name = user_name,email = user_email,text = user_text)
        return redirect('cont')
    us_list = Us.objects.all()
    projectss_list=projectss.objects.all()
    serv_list=serv.objects.all()
    product_list = product.objects.all()
    about_list = about.objects.all()
    return render(request,'main/Index.html',context={
        'product_list':product_list,
        'serv_list':serv_list,
        'about_list':about_list,
        'projectss_list':projectss_list,
        'us_list':us_list
    })
    
def service(request):
    product_list = product.objects.all()
    serv_list=serv.objects.all()
    return render(request,'main/Service.html',context={
        'product_list':product_list,
        'serv_list':serv_list
    })
    
def About(request):
    product_list = product.objects.all()
    about_list = about.objects.all()
    return render(request,'main/About.html',context={
        'product_list':product_list,
        'about_list':about_list
    })
    
def project(request):
    product_list = product.objects.all()
    projectss_list=projectss.objects.all()
    return render(request,'main/Project.html',context={
        'product_list':product_list,
        'projectss_list':projectss_list
    })
    
def testimonial(request):
    product_list = product.objects.all()
    return render(request,'main/Testimonial.html',context={
        'product_list':product_list
    })
    
def contact(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_text = request.POST.get('text')
        cont.objects.create(name = user_name,email = user_email,text = user_text)
        return redirect('cont')
    return render(request,'main/contact.html',context={
        
    })
   
def Menu (request):
    menu_list=menu.object.all()
    return render(request,'base.html',context={
        'menu_list' : menu_list
    })
    
def Flag (request):
    flag_list=flag.objects.all()
    return render(request,'base.html',context={
        'flag_list' : flag_list
    })   
    
    
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm    
    
    
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
   
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")
    