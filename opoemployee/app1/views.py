from django.shortcuts import render,redirect
from app1.models import Employee
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout
from django.contrib import messages
from django.http import HttpResponse


				
def home(request):
	return render(request,'home.html')


def login(request):
	if(request.method == 'GET'):
		return render(request,'login.html')

	else:
		name=request.POST.get('name')
		password=request.POST.get('password')

		try:
			user=Employee.objects.get(name=name)
			flag = check_password(password=password,encoded=user.password)
			if flag:
				temp={}
				temp['name']=user.name
				temp['id']=user.id
				request.session['user']=temp
				return redirect('home')
			else:
				return render(request,'login.html',{'error' :' Email or Password Invalid'})
			
		except:
			return render(request,'login.html',{'error' :' Email or Password Invalid'})


	

def signup(request):
	if(request.method == 'POST'):
		try:
			name=request.POST.get('name')
			
			phone_number=request.POST.get('designation')
			
			password=request.POST.get('password')
			hashedpassword=make_password(password=password)
			email=request.POST.get('email')
			emp=Employee(name=name,phone_number=phone_number,password=hashedpassword,email=email)
			sl=Employee.objects.all()
			emplist=[]
			for i in sl:
				emplist.append(i.email)
			if email not in emplist:
				result=emp.save()
				return redirect('login')
			else:
				return render(request,"error.html")
		except:
			return render(request,'signup.html')

	return render(request,'signup.html')


def signout(request):
	request.session.clear()
	return redirect('home')






