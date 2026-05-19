from django import forms
from .models import UserProfile

class UserProfileUpdateForm(forms.ModelForm): 
    picture = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta: 
        fields = ["profile_picture"]
        model = UserProfile
        widgets = {
        'profile_picture': forms.FileInput(attrs={'class': 'block w-full text-sm text-black file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 '
                                                     'file:text-sm file:font-semibold file:bg-pink-500 file:text-white hover:file:bg-pink-600'})

    }