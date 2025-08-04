from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomAuthenticationForm
from .models import User
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard_view(request):
    role = request.user.role
    if role in ['UESO', 'COORDINATOR', 'DEAN', 'PROGRAM_HEAD', 'DIRECTOR', 'VP']:
        return render(request, 'base_internal.html')
    else:
        return render(request, 'base_public.html')
