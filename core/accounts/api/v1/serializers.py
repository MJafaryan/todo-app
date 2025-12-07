from rest_framework import serializers
from accounts.models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    """The serializer of User Model of program users."""

    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = UserModel
        fields = ["username", "email", "password", "password2"]

    def validate(self, attrs):
        """Validate two passwords are equal or no."""

        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords didn't match."})


        return attrs

    def create(self, validated_data):
        """Create a User from UserModel."""

        user = UserModel.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        return user
