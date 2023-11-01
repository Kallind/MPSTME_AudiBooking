from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('book_auditorium/', views.book_auditorium, name='book_auditorium'),
    path('book_seat/', views.book_seat, name='book_seat'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('',views.index, name="home_page"),
    path('auditorium_events/', views.list_auditorium_events, name='list_auditorium_events'),
    path('seat_booking/<int:event_id>/', views.seat_booking, name='seat_booking'),
]
