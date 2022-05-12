from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import json


def about(request):
	page = ''
	context={}
	return render(request,'myapp/about.html',context)

def applications(request):
	return render(request,'myapp/applications.html')

def contacts(request):
	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
 
		name = body['name']
		email = body['email']
		message = body['message']

		send_mail(name,message,email,['testmail@gmail.com'], fail_silently = False)
		return render(request,'myapp/contacts.html')
	else:
		return render(request,'myapp/contacts.html')

def home(request):
	return render(request,'home.html')