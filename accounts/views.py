from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from .models import CustomUser
from .forms import CustomUserCreationForm, ChangePasswordForm, UserDetailsUpdateForm, ResetPasswordForm, CustomSetPasswordForm
from django.shortcuts import redirect, render


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' # the registration folder is where django searches for the login template by default

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home') # to prevent signed in users from accessing the sign up page

        return super().dispatch(request, *args, **kwargs)


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy("password_change_done")
    template_name = "registration/password_change_form.html" # change if you don't want to use the default template name


class ResetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm

class CustomPasswordResetConfirmView(PasswordResetConfirmView): # view for entering and confirming new password
    form_class = CustomSetPasswordForm


class UserDetailsView(UpdateView):
    template_name = 'user.html'
    form_class = UserDetailsUpdateForm
    model = CustomUser
    
    def get(self, request, *args, **kwargs):
        initial = {'username': request.user.username, 'first_name': request.user.first_name, 'last_name': request.user.last_name}
        form = self.form_class(initial=initial) # Initial fields with default values if request is a get request
        return render(request, self.template_name, {'form': form})


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home') # to prevent signed in users from accessing the sign up page

        return super().dispatch(request, *args, **kwargs)