from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    property_title = serializers.ReadOnlyField(source='property.title')

    class Meta:
        model = Booking
        fields = ['id', 'property', 'property_title', 'user', 'check_in_date', 'check_out_date', 'total_price', 'status', 'created_at']
