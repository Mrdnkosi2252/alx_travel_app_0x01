from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.utils import timezone
import uuid

class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def handle(self, *args, **options):
        # Delete existing data to avoid duplicates
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()

      
        listings_data = [
            {
                'title': 'Cozy Beach Cottage',
                'description': 'A beautiful cottage by the sea.',
                'price_per_night': 150.00,
                'location': 'Miami, FL',
            },
            {
                'title': 'Mountain Retreat',
                'description': 'Peaceful retreat in the mountains.',
                'price_per_night': 200.00,
                'location': 'Aspen, CO',
            },
        ]

        # Create listings
        listings = [Listing(**data) for data in listings_data]
        listings = Listing.objects.bulk_create(listings)

      
        bookings_data = [
            {
                'listing': listings[0],
                'user_email': 'john.doe@example.com',
                'check_in_date': timezone.now().date() + timezone.timedelta(days=1),
                'check_out_date': timezone.now().date() + timezone.timedelta(days=5),
            },
            {
                'listing': listings[1],
                'user_email': 'jane.smith@example.com',
                'check_in_date': timezone.now().date() + timezone.timedelta(days=7),
                'check_out_date': timezone.now().date() + timezone.timedelta(days=10),
            },
        ]

       
        Booking.objects.bulk_create([Booking(**data) for data in bookings_data])

       
        reviews_data = [
            {
                'listing': listings[0],
                'user_email': 'john.doe@example.com',
                'rating': 4,
                'comment': 'Great location, loved the view!',
            },
            {
                'listing': listings[1],
                'user_email': 'jane.smith@example.com',
                'rating': 5,
                'comment': 'Amazing experience, highly recommend!',
            },
        ]

        # Create reviews
        Review.objects.bulk_create([Review(**data) for data in reviews_data])

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))