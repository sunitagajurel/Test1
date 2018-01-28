from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
	return render(request,'accounts/home.html')

def login_redirect(request):
	return redirect('/accounts/')

def register(request):
	if request.method =='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts/')
	else:
		form = RegistrationForm()
		args ={'form': form}
		return render(request,'accounts/reg_form.html',args)

def profile(request):
	args = {'user':request.user}
	return render(request,'accounts/profile.html',args)
