from django.urls import path
from .views import BookingCreateView, BookingListView

app_name = 'bookings'

urlpatterns = [
    path('', BookingListView.as_view(), name='list'),
    path('<int:property_id>/create/', BookingCreateView.as_view(), name='create'),
]
