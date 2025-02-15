from datetime import timedelta
from django.utils import timezone
from bookings.models import Movie, Session, Booking
from users.models import User

# ایجاد یک فیلم
movie = Movie.objects.create(
    title="فیلم تست",
    age_rating=12,
    duration=timedelta(hours=2),  # مدت زمان فیلم به صورت timedelta
    description="این یک فیلم تست است"
)

# ایجاد یک سانس با تاریخ و زمان همراه با منطقه زمانی
start_time = timezone.make_aware(timezone.datetime(2023, 10, 15, 18, 0, 0))
end_time = timezone.make_aware(timezone.datetime(2023, 10, 15, 20, 0, 0))

session = Session.objects.create(
    movie=movie,
    start_time=start_time,
    end_time=end_time,
    capacity=100
)

# ایجاد یک کاربر
user = User.objects.create_user(
    email='tki@example.com',
    birthdate='2000-01-01',
    password='testpass123'
)

# رزرو سانس
booking = Booking.objects.create(user=user, session=session)
print(booking)  # باید رزرو نمایش داده شود