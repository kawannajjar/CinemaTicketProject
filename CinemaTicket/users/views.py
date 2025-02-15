from django.shortcuts import render, redirect
import logging
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm  # وارد کردن فرم




logger = logging.getLogger(__name__)



def test_log(request):
    logger.debug('این یک لاگ تست است!')
    return HttpResponse('لاگ تست با موفقیت ثبت شد.')


@login_required
def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "پروفایل شما با موفقیت به‌روزرسانی شد.")
            return redirect('profile')
    else:
        form = UserRegistrationForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # بعد از ثبت‌نام به صفحه پروفایل هدایت می‌شود
    else:
        form = UserRegistrationForm()
    return render(request, 'users/signup.html', {'form': form})