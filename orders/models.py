from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Order(models.Model):
    apartment_number = models.CharField(max_length=10)
    pet_name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    start_time = models.DateTimeField()

    def clean(self):
        if self.start_time.hour < 7 or self.start_time.hour > 23:
            raise ValidationError("Time must be between 7:00 and 23:00.")
        if self.start_time.minute not in [0, 30]:
            raise ValidationError("Start time must be on the hour or half past.")
        end_time = self.start_time + timezone.timedelta(minutes=30)
        orders = Order.objects.filter(start_time__lt=end_time, start_time__gt=self.start_time)
        if orders.exists():
            raise ValidationError("There is already an order that overlaps with this time.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order: {self.apartment_number} - {self.pet_name}"