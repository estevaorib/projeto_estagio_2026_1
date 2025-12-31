from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

BASE_INPUT_CLASS = (
    "w-full rounded-lg py-2 px-3 h-14 border border-slate-700 bg-slate-800 text-white placeholder-[#92adc9] focus:outline-none focus:border-blue-500 transition-colors"
)

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={
            "class": BASE_INPUT_CLASS,
            "placeholder": "Digite seu usuário"
        })
    )

    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            "class": BASE_INPUT_CLASS,
            "placeholder": "********"
        })
    )

    error_messages = {
        "invalid_login": _(
            "Usuário ou senha inválidos!"
        ),
    }
