from django.db import models

class AuditoriumEvent(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    expected_attendees = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.event_name

class SeatBooking(models.Model):
    event = models.ForeignKey(AuditoriumEvent, related_name='seat_bookings', on_delete=models.CASCADE, null=True, blank=True)
    seat_row = models.IntegerField(null=True, blank=True)
    seat_column = models.IntegerField(null=True, blank=True)
    attendee_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.seat_row}-{self.seat_column}"

