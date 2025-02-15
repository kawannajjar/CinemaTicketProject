from django.test import TestCase, Client
from django.urls import reverse
from .models import Movie, Session, Booking
from users.models import User
from datetime import timedelta

class BookingModelTest(TestCase):
    def setUp(self):
        # ایجاد یک فیلم
        self.movie = Movie.objects.create(
            title="فیلم تست",
            age_rating=12,
            duration=timedelta(hours=2),
            description="این یک فیلم تست است"
        )

        # ایجاد یک سانس
        self.session = Session.objects.create(
            movie=self.movie,
            start_time="2023-10-15 18:00:00",
            end_time="2023-10-15 20:00:00",
            capacity=100
        )

        # ایجاد یک کاربر
        self.user = User.objects.create_user(
            email='test@example.com',
            birthdate='2000-01-01',
            password='testpass123'
        )

    def test_session_creation(self):
        """بررسی ایجاد سانس"""
        self.assertEqual(self.session.movie.title, "فیلم تست")
        self.assertEqual(self.session.capacity, 100)

    def test_booking_creation(self):
        """بررسی ایجاد رزرو"""
        booking = Booking.objects.create(user=self.user, session=self.session)
        self.assertEqual(booking.user.email, 'test@example.com')
        self.assertEqual(booking.session.movie.title, "فیلم تست")

    def test_session_is_full(self):
        """بررسی پر بودن سانس"""
        for _ in range(100):  # رزرو تمام صندلی‌ها
            Booking.objects.create(user=self.user, session=self.session)
        self.assertTrue(self.session.is_full())