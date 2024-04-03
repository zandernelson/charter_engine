from django.db import models
import uuid

# MODELS

# BOOKING MODEL

class Booking(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)
    confirmation_number = models.CharField(max_length=36, default=uuid.uuid4, unique=True)

    
