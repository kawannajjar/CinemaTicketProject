from django.urls import path
from . import views


urlpatterns = [
    path('sessions/', views.session_list, name='session-list'),
    path('book/<int:session_id>/', views.book_session, name='book-session'),
]