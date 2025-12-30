from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def landpage(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST.get('name'),
            institution=request.POST.get('institution'),
            job_title=request.POST.get('job_title'),
            email=request.POST.get('email'),
            message=request.POST.get('message'),
            submit_date = timezone.now()
        )
        
        contact.save()

        return redirect('thank_you')

    return render(request, 'landpage.html')


def thank_you(request):
    return render(request, 'thank_you.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            return redirect('/admin/')
        else:
            return HttpResponse('nao autenticado')
    else:
        return render(request, 'login.html')
    
@login_required(login_url='login')    
def panel(request):
    messages = Contact.objects.all().order_by('submit_date')
    return render(request, 'panel.html', {
        'messages': messages
    })