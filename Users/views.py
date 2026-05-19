from .models import UserProfile
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django import forms
from .forms import UserProfileUpdateForm

@method_decorator(login_required, name='dispatch')
class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "users/user_detail.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_loans"] = self.object.user.loans.filter(returned=False).select_related("book")
        return context


@method_decorator(login_required, name='dispatch')
class UserProfileUpdateView(UpdateView): 
    model = UserProfile
    template_name = "users/user_update.html"
    form_class = UserProfileUpdateForm
    context_object_name = "profile"
    
    def get_success_url(self):
        return reverse('user-profile', args=[self.object.pk])