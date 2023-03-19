from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.
#URL DISPATCHER
def index(request):
    #return HttpResponse("This is homepage")
    context = {
        'variable':"this is sent",
        'variable1':"dipti"
    }

    return render(request,'index.html')

def about(request):
    #return HttpResponse("This is aboutpage")
     return render(request,'about.html')


def services(request):
    #return HttpResponse("This is service page")
    return render(request,'services.html')


def contact(request):
   # return HttpResponse("This is contact page")
   if request.method == "POST":

    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    #desc = request.POST.get('desc')
    contact = Contact(name=name,email=email,phone=phone,date = datetime.today())
    contact.save()
    messages.success(request, 'Your mesaage has been sent!')
   return render(request,'contact.html')
