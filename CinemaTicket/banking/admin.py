from django.contrib import admin
from .models import BankAccount

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'user', 'balance')
    search_fields = ('account_number', 'user__email')