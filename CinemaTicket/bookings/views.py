from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Session, Booking
from users.models import User
import logging




logger = logging.getLogger(__name__)

def book_session(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    user = request.user

    # بررسی رده سنی کاربر
    if user.age < session.movie.age_rating:
        messages.error(request, "شما مجاز به رزرو این سانس نیستید (محدودیت سنی).")
        return redirect('session-list')

    # بررسی ظرفیت سالن
    if session.is_full():
        messages.error(request, "سالن پر است.")
        return redirect('session-list')

    # اعمال تخفیف (اگر کاربر اشتراک داشته باشد)
    price = 10000  # قیمت پیش‌فرض بلیت
    if hasattr(user, 'subscription'):
        price = user.subscription.apply_discount(price)

    # ایجاد رزرو
    Booking.objects.create(user=user, session=session)
    messages.success(request, f"سانس با موفقیت رزرو شد. قیمت نهایی: {price} تومان")
    return redirect('session-list')


def session_list(request):
    sessions = Session.objects.all()
    
    for session in sessions:
        session.remaining_capacity = session.capacity - session.booked_seats  # مقدار محاسبه‌شده

    return render(request, 'bookings/session_list.html', {'sessions': sessions})
