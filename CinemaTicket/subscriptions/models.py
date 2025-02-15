from django.db import models
from users.models import User

class SubscriptionType(models.TextChoices):
    BRONZE = 'Bronze', 'برنزی'
    SILVER = 'Silver', 'نقرهای'
    GOLD = 'Gold', 'طلایی'

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscription')
    sub_type = models.CharField(
        max_length=10,
        choices=SubscriptionType.choices,
        default=SubscriptionType.BRONZE
    )
    start_date = models.DateField(auto_now_add=True)

    def apply_discount(self, amount):
        """اعمال تخفیف بر اساس نوع اشتراک"""
        if self.sub_type == SubscriptionType.SILVER:
            return amount * 0.8  # 20% تخفیف
        elif self.sub_type == SubscriptionType.GOLD:
            return amount * 0.5  # 50% تخفیف
        return amount  # بدون تخفیف

    def __str__(self):
        return f"Subscription {self.sub_type} (User: {self.user.email})"