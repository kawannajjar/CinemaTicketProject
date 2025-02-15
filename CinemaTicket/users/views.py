from django.http import HttpResponse
import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login 
from .forms import UserRegistrationForm





@login_required
def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})


logger = logging.getLogger(__name__)

def test_log(request):
    logger.debug('این یک لاگ تست است!')
    return HttpResponse('لاگ تست با موفقیت ثبت شد.')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "پروفایل شما با موفقیت به‌روزرسانی شد.")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})

def signup_view(request):  # یا def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # بعد از ثبت‌نام به صفحه پروفایل هدایت می‌شود
    else:
        form = UserRegistrationForm()
    return render(request, 'users/signup.html', {'form': form})