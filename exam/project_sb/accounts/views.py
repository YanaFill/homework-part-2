from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Акаунт для {username} створено!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Відображення профілю для залогованих користувачів
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


# Вихід з акаунту
def user_logout(request):
    logout(request)
    return redirect('subject_list')