from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_id', 'title', 'description', 'price_per_night', 'location', 'created_at']
        read_only_fields = ['listing_id', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['booking_id', 'listing', 'user_email', 'check_in_date', 'check_out_date', 'created_at']
        read_only_fields = ['booking_id', 'created_at']