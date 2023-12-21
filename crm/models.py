from django.db import models

class Record(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)  # Assuming a basic phone number format, adjust if needed
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)  # Assuming a basic ZIP code format, adjust if needed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
