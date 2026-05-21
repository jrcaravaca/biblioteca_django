from .models import UserProfile
from django.views.generic import DetailView, UpdateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django import forms
from .forms import UserProfileUpdateForm
from Library.models.loan_model import Loan


@method_decorator(login_required, name='dispatch')
class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "users/user_detail.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_loans"] = self.object.user.loans.filter(returned=False).select_related("book")
        context["loans"] = self.object.user.loans.select_related("book").order_by("-created_at")[:10]
        return context


@method_decorator(login_required, name='dispatch')
class UserProfileUpdateView(UpdateView): 
    model = UserProfile
    template_name = "users/user_update.html"
    form_class = UserProfileUpdateForm
    context_object_name = "profile"
    
    def get_success_url(self):
        return reverse('user-profile', args=[self.object.pk])
    
@method_decorator(login_required, name='dispatch')
class UserHistoryView(ListView): 
    model = Loan
    template_name = "users/user_history.html"
    context_object_name = "loans"
    paginate_by = 15

    def get_queryset(self): 
        return Loan.objects.all().select_related('user', 'book').order_by('-created_at')
    