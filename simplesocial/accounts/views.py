from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateFrom
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"



