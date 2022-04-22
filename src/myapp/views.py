from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
	page = ''
	context={}
	return render(request,'myapp/about.html',context)

def applications(request):
	return render(request,'myapp/applications.html')

def contacts(request):
	return render(request,'myapp/contacts.html')
def home(request):
	return render(request,'home.html')