from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    property_title = serializers.ReadOnlyField(source='property.title')

    class Meta:
        model = Review
        fields = ['id', 'property', 'property_title', 'user', 'rating', 'comment', 'created_at']
