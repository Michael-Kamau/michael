from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from smtplib import SMTPException
from decouple import config

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

	
		try:
			send_mail(name,'Email: '+email+'\nMessage: '+message,config('EMAIL_FROM_ADDRESS'),['kamau.karitu@gmail.com'], fail_silently = False)

			return JsonResponse({'status':200, 'success': True})

		except  Exception as e:

			return JsonResponse({'status':200, 'success': False,'error':str(e)})

	else:
		return render(request,'myapp/contacts.html')

def home(request):
	return render(request,'home.html')