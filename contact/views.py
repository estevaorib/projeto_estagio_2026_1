from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact

def landpage(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST.get('name'),
            institution=request.POST.get('institution'),
            job_title=request.POST.get('job_title'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        
        contact.save()

        return redirect('thank_you')

    return render(request, 'landpage.html')


def thank_you(request):
    return render(request, 'thank_you.html')
