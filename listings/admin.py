from django.contrib import admin
from .models import Listing, Booking, Review

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('listing_id', 'title', 'location', 'price_per_night', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('location', 'created_at')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'listing', 'user_email', 'check_in_date', 'check_out_date', 'created_at')
    search_fields = ('user_email', 'listing__title')
    list_filter = ('check_in_date', 'check_out_date', 'created_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'listing', 'user_email', 'rating', 'created_at')
    search_fields = ('user_email', 'listing__title')
    list_filter = ('rating', 'created_at')
