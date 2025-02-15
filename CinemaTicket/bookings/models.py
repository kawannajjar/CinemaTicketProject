from django.db import models
from users.models import User



# مدل Movie
class Movie(models.Model):
    title = models.CharField(max_length=255)
    age_rating = models.PositiveIntegerField()  # رده سنی فیلم
    duration = models.DurationField()  # مدت زمان فیلم
    description = models.TextField()

    def __str__(self):
        return self.title


# مدل Session
class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField()  # زمان شروع سانس
    end_time = models.DateTimeField()  # زمان پایان سانس
    capacity = models.PositiveIntegerField()  # ظرفیت سالن
    booked_seats = models.PositiveIntegerField(default=0)  # تعداد صندلی‌های رزرو شده

    def is_full(self):
        """آیا سالن پر شده است؟"""
        return self.booked_seats >= self.capacity

    def __str__(self):
        return f"{self.movie.title} - {self.start_time}"


# مدل Booking
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    session = models.ForeignKey('Session', on_delete=models.CASCADE, related_name='bookings')  # استفاده از رشته به جای مدل
    booking_time = models.DateTimeField(auto_now_add=True)  # زمان رزرو

    def save(self, *args, **kwargs):
        """بررسی ظرفیت سالن قبل از ذخیره رزرو"""
        if self.session.is_full():
            raise ValueError("سالن پر است")
        self.session.booked_seats += 1
        self.session.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking by {self.user.email} for {self.session.movie.title}"