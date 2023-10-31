from django.db import models

class AuditoriumEvent(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    expected_attendees = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.event_name

class SeatBooking(models.Model):
    seat_row = models.IntegerField()
    seat_column = models.IntegerField()
    attendee_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.seat_row}-{self.seat_column}"
