from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer_user

# Signup form
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit)
        phone = self.cleaned_data.get('phone')
        if commit:
            Customer_user.objects.create(user=user, phone=phone)
        return user

# Update User model fields
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

# Update Customer_user profile fields
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer_user
        fields = ['phone']
