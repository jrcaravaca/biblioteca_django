from django import forms
from django.contrib.auth.models import User



class RegistrationForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput())
    dni = forms.CharField(label="DNI")
    class Meta: 
        model = User
        fields = [
            "first_name",
            "last_name",
            "username", 
            "email", 
            "password"
        ]

    def save(self): 
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password"])
        user.save()

        from Users.models import UserProfile
        UserProfile.objects.create(user=user, dni=self.cleaned_data["dni"])

        return user

class LoginForm(forms.Form): 
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())