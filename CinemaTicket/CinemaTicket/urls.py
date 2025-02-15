from django.urls import path
from users.views import test_log  # وارد کردن تابع test_log

urlpatterns = [
    path('test-log/', test_log, name='test-log'),
]