from django.shortcuts import render

# Create your views here.

def home(request):
	test = "Hey ange this is my firts blog"
	return render(request, "index.html", locals())
def contact(request):
	return render(request, "contact.html", locals())
def about(request):
	return render(request,"moi.html",locals())
def myname(request):
	return render(request,"ange.html",locals())