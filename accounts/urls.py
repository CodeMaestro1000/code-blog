from django.urls import path
from .views import SignUpView, ChangePasswordView, UserDetailsView, ResetPasswordView, CustomPasswordResetConfirmView
from django.contrib.auth.views import LoginView
from .forms import LoginForm

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True, authentication_form=LoginForm), name='login'), # no need to specify template name because Django searches in registration by default
    path('user_data/<int:pk>', UserDetailsView.as_view(), name='user_info'),
    path("password_change/", ChangePasswordView.as_view(), name="password_change"),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path("reset/<uidb64>/<token>/", CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]