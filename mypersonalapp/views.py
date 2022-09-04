from turtle import setundobuffer
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == "POST":
        fullname= request.POST['fullname']
        message_email =  request.POST['email']
        content_message = request.POST['message']
        
        send_mail(
            'Enquiry from ' + fullname,
            content_message,
            message_email,
            ['june.mphahlele@gmail.com']
        )
        return render(request,'home.html',{'fullname':fullname})

    else: 
        return render(request,'home.html',{})