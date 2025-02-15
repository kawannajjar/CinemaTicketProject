from django.urls import path
from django.contrib import admin
from django.urls import path, include
from users.views import test_log  # وارد کردن تابع test_log
from bookings.views import home  # وارد کردن ویو صفحه اصلی


urlpatterns = [
    path('test-log/', test_log, name='test-log'),
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),  # صفحه اصلی


]