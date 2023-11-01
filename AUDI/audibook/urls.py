from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('book_auditorium/', views.book_auditorium, name='book_auditorium'),
    path('book_seat/', views.book_seat, name='book_seat'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('',views.index, name="home_page")
]
