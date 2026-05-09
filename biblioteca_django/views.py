from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from Library.models.book_model import Book
from django.contrib.auth.models import User

from .forms import LoginForm, RegistrationForm

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView): 
    template_name = 'general/home.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        books = Book.objects.order_by('-id')[:6]
        context['books'] = books
        
        return context
    

class LoginView(FormView):
    template_name = "general/login.html"
    form_class = LoginForm
    
    def form_valid( self, form): 
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=password)

        if user is not None: 
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, f"Bienvenido de nuevo {user.username}")
            return HttpResponseRedirect( reverse('home') )
        else: 
            messages.add_message(self.request, messages.ERROR, 'Usuario no válido o contraseña no válida')
            return super(LoginView, self).form_invalid(form)
        


class RegisterView(CreateView):
    template_name = "general/register.html"
    model = User
    success_url = reverse_lazy('login')
    form_class = RegistrationForm

    def form_valid(self, form): 
        messages.add_message(self.request, messages.SUCCESS, "Usuario creado correctamente")
        return super(RegisterView, self).form_valid(form)

   
@login_required
def logout_view(request): 
    logout(request)
    messages.add_message(request, messages.INFO, "Se ha cerrado sesión correctamente")
    return HttpResponseRedirect(reverse('home'))