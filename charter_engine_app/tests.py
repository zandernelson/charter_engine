from django.test import TestCase
from .models import Booking
from django.utils import timezone

# TESTS

# MODEL TESTS

# BOOKING TESTS

class BookingModelTestCase(TestCase):
    def setUp(self):
        print("BookingModelTestCase...")
        self.booking = Booking.objects.create(
            start_time = timezone.now(),
            end_time = timezone.now() + timezone.timedelta(hours=2)
        )

    def test_booking_model(self):
        self.assertTrue(isinstance(self.booking, Booking))
        self.assertIsNotNone(self.booking.start_time)
        self.assertIsNotNone(self.booking.end_time)
        self.assertIsNotNone(self.booking.creation_time)
        self.assertIsNotNone(self.booking.confirmation_number)