from django.contrib import admin
from .models import Movie, Session, Booking

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'age_rating', 'duration')
    search_fields = ('title',)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'start_time', 'end_time', 'capacity', 'booked_seats')
    search_fields = ('movie__title',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'booking_time')
    search_fields = ('user__email', 'session__movie__title')