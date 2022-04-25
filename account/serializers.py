from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'position']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            position=validated_data['position'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
