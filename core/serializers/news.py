from abc import ABC

from rest_framework import serializers


class NewsSerializer(serializers.Serializer, ABC):
    """
    Serialize a news object
    """
    name = serializers.CharField()
    date = serializers.DateField()
    article = serializers.CharField()
    website = serializers.BooleanField()
    author = serializers.CharField()
    image_url = serializers.URLField(required=False, read_only=True)

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        pass
