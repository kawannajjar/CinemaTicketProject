from django.contrib import admin
from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sub_type', 'start_date')
    search_fields = ('user__email', 'sub_type')