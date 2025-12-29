from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def landpage(request):
    if request.method == 'GET':
        return render(request, 'landpage.html')
    else:
        name = request.POST.get('name')
        institution = request.POST.get('institution')
        job_title = request.POST.get('job_title')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(
            name = name,
            institution = institution,
            job_title = job_title,
            email = email,
            message = message
        )

        return HttpResponse('Criado')