from django.shortcuts import render,redirect
from django .core .mail import send_mail
from django.contrib import messages
# Create your views here.
from  portfolioapp .models import Links,Skills,Projects
def home(request):
    skill=Skills.objects.all()
    links=Links.objects.all()
    project=Projects.objects.all()

    context={
        "skill":skill,
        "links":links,
        "project":project
    }
    
    if request.method=='POST':
        name=request.POST.get('name')
        number=request.POST.get('number')
        email=request.POST.get('info')
        info=request.POST.get('message')
        # print(name,email,info,number)
        email_info={
            'name':name,
            'number':number,
            'email':email,
            'info':info,
        }
        # print(email_info)
        inside_email='''
        Name:{}
        New message:{}
        From:{}
        Number:{}
        '''.format(email_info['name'],email_info['info'],email_info['email'],email_info['number'])
        if inside_email is not None:
            send_mail(name,inside_email,'',["jobinj5210@gmail.com"])
            messages.success(request,'Succsesfully sented')
            return redirect(home)
        else:
            messages.error(request,"send failed")
    
    return render(request,'home.html',context)