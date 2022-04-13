from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, 
                                        PasswordResetForm, SetPasswordForm)
from django.contrib.auth import password_validation
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = { 'class': 'form-control form-input', 'id': 'username-field' }
        self.fields['first_name'].widget.attrs = { 'class': 'form-control form-input', 'id': 'first-name-field' }
        self.fields['last_name'].widget.attrs = { 'class': 'form-control form-input', 'id': 'last-name-field' }
        self.fields['email'].widget.attrs = { 'class': 'form-control form-input' }
        self.fields['password1'].widget.attrs = { 'class': 'form-control form-input', 'id': 'password-field' }
        self.fields['password2'].widget.attrs = { 'class': 'form-control form-input', 'id': 'confirm-password-field' }

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    # Change the label of the second password field from Password Confirmation (default) to Confirm Password
    password2 = forms.CharField(
        label='Confirm Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username')
        error_messages = {
            'username': {'unique': ("Username already taken, please choose another one")},
            'email': {'unique': ("An account with this email already")}
        }


class CustomUserChangeForm(UserChangeForm): # Shows up in Django Admin
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'username')


class LoginForm(AuthenticationForm): # for styling the login form
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-input'}))

    error_messages = {
        'invalid_login': (
            "Invalid Username or Password"
        ),
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs = { 'class': 'form-control form-input', 'id': 'current-password' }
        self.fields['new_password1'].widget.attrs = { 'class': 'form-control form-input', 'id': 'new-password' }
        self.fields['new_password2'].widget.attrs = { 'class': 'form-control form-input', 'id': 'confirm-new-password' }
    
    old_password = forms.CharField(
        label='Current Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_texts(), # override default behaviour to return a list instead
    )


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs = { 'class': 'user-data-input' }


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs = { 'class': 'user-data-input' }
        self.fields['new_password2'].widget.attrs = { 'class': 'user-data-input' }

    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_texts(), # override default behaviour to return a list instead
    )

    new_password2 = forms.CharField(
        label= "Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )


class UserDetailsUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserDetailsUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = { 'class': 'user-data-input' }
        self.fields['first_name'].widget.attrs = { 'class': 'user-data-input'}
        self.fields['last_name'].widget.attrs = { 'class': 'user-data-input'}

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name']
