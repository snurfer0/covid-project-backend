from rest_framework import serializers
from .models import Test, User
from django.conf import settings as api_settings


class TestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `test` instance, given the validated data.
        """
        return Test.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `test` instance, given the validated data.
        """
        instance.image = validated_data.get('image', instance.image)
        instance.isPositive = validated_data.get(
            'isPositive', instance.isPositive)
        instance.save()
        return instance

    class Meta:
        model = Test
        fields = ['id', 'image', 'isPositive',
                  'timestamp', 'owner']


class UserSerializer(serializers.ModelSerializer):
    tests = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Test.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tests']
