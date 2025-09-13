from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView



class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "user/register.html"
    success_url = reverse_lazy("landing")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request,user)
        return response

class SignInView(LoginView):
    template_name = 'user/signin.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('landing')

class SignOutView(LogoutView):
    next_page = reverse_lazy('landing')

