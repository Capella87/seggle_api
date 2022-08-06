from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Announcement.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_important = validated_data.get('important', instance.is_important)
        instance.is_visible = validated_data.get('visible', instance.is_visible)

        instance.save()
        return instance

    class Meta:
        model = Announcement
        fields = [
            'pk',
            'writer',
            'title',
            'description',
            'created_time',
            'last_modified',
            'is_important',
            'is_visible',
        ]