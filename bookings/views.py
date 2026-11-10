from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Booking
from properties.models import Property

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'
    
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-created_at')

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'bookings/booking_form.html'
    fields = ['check_in_date', 'check_out_date']
    success_url = reverse_lazy('bookings:list')

    def form_valid(self, form):
        property_obj = get_object_or_404(Property, id=self.kwargs['property_id'])
        form.instance.property = property_obj
        form.instance.user = self.request.user
        
        # Простой расчет цены (кол-во дней * цена)
        days = (form.instance.check_out_date - form.instance.check_in_date).days
        if days < 1:
            days = 1
        form.instance.total_price = days * property_obj.price_per_night
        
        return super().form_valid(form)
