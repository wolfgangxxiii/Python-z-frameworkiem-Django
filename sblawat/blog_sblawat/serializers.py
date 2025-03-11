from rest_framework import serializers
from .models import PostSblawat

class PostSblawatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSblawat
        fields = '__all__'
