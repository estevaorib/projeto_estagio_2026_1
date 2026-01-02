from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


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

        request.session['form_submitted'] = True
        
        contact.save()

        return redirect('thank_you')

    return render(request, 'landpage.html',{
        'menu_buttons': True
    })


def thank_you(request):
    if request.session.get('form_submitted'):
        del request.session['form_submitted']

        return render(request, 'thank_you.html')
    
    return redirect('landpage')
    
@login_required(login_url='login')    
def panel(request):
    contacts_list = Contact.objects.all().order_by('submit_date')

    paginator = Paginator(contacts_list, 4)
    page_number = request.GET.get('page')

    contacts = paginator.get_page(page_number)

    return render(request, 'panel.html', {
        'contacts': contacts
    })