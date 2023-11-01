from django import forms
from .models import AuditoriumEvent

from django import forms
from .models import AuditoriumEvent

class AuditoriumEventForm(forms.ModelForm):
    class Meta:
        model = AuditoriumEvent
        fields = ['event_name', 'event_description', 'expected_attendees', 'booking_date']
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control'}),
            'expected_attendees': forms.NumberInput(attrs={'class': 'form-control'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


from django import forms
from .models import SeatBooking

class SeatBookingForm(forms.ModelForm):
    class Meta:
        model = SeatBooking
        fields = ['event', 'seat_row', 'seat_column', 'attendee_name', 'contact_info']
        widgets = {
            'attendee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_info': forms.TextInput(attrs={'class': 'form-control'}),
        }

