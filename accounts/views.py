from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView

# Signup View


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
    template_name = 'signup.html'


# Login View (using Django's built-in LoginView)
class CustomLoginView(LoginView):
    template_name = 'login.html'


# Logout View (using Django's built-in LogoutView)
class CustomLogoutView(LogoutView):
    next_page = 'task'  # Redirect after logout
