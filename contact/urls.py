from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from contact.forms import LoginForm

app_name = "contacts"

urlpatterns = [
    path("", views.landpage, name='landpage'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('login/', LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('panel/', views.panel, name='panel'),
    path('logout/', LogoutView.as_view(next_page='contacts:landpage'), name='logout'),
    path('edit/<int:id>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
]