from rest_framework import serializers import ModelSerializer
from .models import Review

class ReviewSerializer(ModelSerializer):
    class meta:
        model = Review
        fields = "__all__"
