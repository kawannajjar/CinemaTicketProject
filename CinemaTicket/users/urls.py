from django.urls import path
from . import views
from .views import signup_view 


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('signup/', signup_view, name='signup'),
]