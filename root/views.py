from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request , 'root/index.html')

def contact(request):
    return render(request , 'root/contact-us.html')

def about(request):
    return render(request , 'root/about-us.html')



