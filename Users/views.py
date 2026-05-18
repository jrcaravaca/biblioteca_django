from .models import UserProfile
from django.views.generic import DetailView


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "users/user_detail.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_loans"] = self.object.user.loans.filter(returned=False).select_related("book")
        return context
