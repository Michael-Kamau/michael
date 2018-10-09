from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
	return render(request,'myapp/about.html')

def applications(request):
	return render(request,'myapp/applications.html')

def contacts(request):
	return render(request,'myapp/contacts.html')
def home(request):
	return render(request,'home.html')