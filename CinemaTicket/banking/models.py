from django.db import models
from users.models import User

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_accounts')
    account_number = models.CharField(max_length=16, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    password = models.CharField(max_length=128)  # رمز حساب بانکی
    cvv2 = models.CharField(max_length=4)  # کد CVV2

    def withdraw(self, amount):
        """برداشت از حساب"""
        if self.balance < amount:
            raise ValueError("موجودی کافی نیست")
        self.balance -= amount
        self.save()

    def deposit(self, amount):
        """واریز به حساب"""
        self.balance += amount
        self.save()

    def transfer(self, target_account, amount):
        """انتقال وجه به حساب دیگر"""
        self.withdraw(amount)
        target_account.deposit(amount)

    def __str__(self):
        return f"BankAccount {self.account_number} (User: {self.user.email})"