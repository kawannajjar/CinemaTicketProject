from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Session, Booking
from users.models import User
import logging





logger = logging.getLogger(__name__)


from django.shortcuts import render

def home(request):
    return render(request, 'bookings/home.html')

def book_session(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    user = request.user

    # بررسی رده سنی کاربر
    if user.age < session.movie.age_rating:  # استفاده از متد age
        messages.error(request, "شما مجاز به رزرو این سانس نیستید (محدودیت سنی).")
        return redirect('session-list')

    # بررسی ظرفیت سالن
    if session.is_full():
        messages.error(request, "سالن پر است.")
        return redirect('session-list')

    # ایجاد رزرو
    Booking.objects.create(user=user, session=session)
    messages.success(request, "سانس با موفقیت رزرو شد.")
    return redirect('session-list')




def session_list(request):
    sessions = Session.objects.all()
    for session in sessions:
        session.remaining_capacity = session.capacity - session.booked_seats  # محاسبه ظرفیت باقی‌مانده
    return render(request, 'bookings/session_list.html', {'sessions': sessions})
