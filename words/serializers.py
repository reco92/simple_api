
# from django.contrib.admin.models import CHANGE, LogEntry
# from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

class NumberSerializer(serializers.Serializer):

    """Serializer to check params for the convertion."""

    number = serializers.IntegerField()
