from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = ('username', 'password', 'is_staff')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.is_staff=bool(validated_data['is_staff'])
        user.set_password(validated_data['password'])
        user.save()

        return user