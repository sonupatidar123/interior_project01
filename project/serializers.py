from rest_framework import serializers
from .models import Project, ProjectImage
from .models import ContactMessage


class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ProjectImage
        fields = ('id', 'image', 'caption')


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'description',
            'image',
            'images',
            'featured',
            'created_at'
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'phone', 'message', 'created_at']