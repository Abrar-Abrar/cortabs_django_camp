from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address')
    address = forms.CharField(
        max_length=300, help_text='Required. Inform your address')

    class Meta:
        model = User
        fields = ("username", "password1", "password2",
                  "first_name", "last_name", "email", "address")


class EmailValidationBeforeResetPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if not User.objects.filter(email=email, is_active=True).exists():
            raise ValidationError(
                "There is no user registered with this email address")
        return email
