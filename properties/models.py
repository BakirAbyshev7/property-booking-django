from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Property(models.Model):
    PROPERTY_TYPES = (
        ('apartment', 'Апартаменты'),
        ('house', 'Дом'),
        ('villa', 'Вилла'),
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, default='apartment')
    address = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    max_guests = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=500)  # Упрощенно используем URL вместо FileField
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.property.title}"
