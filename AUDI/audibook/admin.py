from django.contrib import admin
from .models import AuditoriumEvent, SeatBooking  # Import both models

@admin.register(AuditoriumEvent)
class AuditoriumEventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'booking_date', 'expected_attendees']

@admin.register(SeatBooking)  # Register the SeatBooking model
class SeatBookingAdmin(admin.ModelAdmin):
    list_display = ['event', 'seat_row', 'seat_column', 'attendee_name', 'is_booked']