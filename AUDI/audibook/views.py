from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AuditoriumEventForm

def book_auditorium(request):
    if request.method == "POST":
        form = AuditoriumEventForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"success.html")
    else:
        form = AuditoriumEventForm()

    return render(request, 'auditorium_booking.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import SeatBookingForm

def book_seat(request):
    if request.method == 'POST':
        form = SeatBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucess.html')  # Redirect to a success or summary page
    else:
        form = SeatBookingForm()

    context = {'form': form}

    return render(request, 'seat-booking.html', {'form': form})

from django.shortcuts import render
from .models import AuditoriumEvent, SeatBooking

def admin_dashboard(request):
    total_auditorium_bookings = AuditoriumEvent.objects.count()
    total_seat_bookings = SeatBooking.objects.count()

    auditorium_bookings = AuditoriumEvent.objects.all()
    seat_bookings = SeatBooking.objects.all()

    context = {
        'total_auditorium_bookings': total_auditorium_bookings,
        'total_seat_bookings': total_seat_bookings,
        'auditorium_bookings': auditorium_bookings,
        'seat_bookings': seat_bookings,
    }

    return render(request, 'admin-dash.html', context)

def index(request):
    return render(request,"index.html")

def success(request):
    return render(request,"success.html")



