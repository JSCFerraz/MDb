from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        if validated_data.get("is_superuser"):
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "bio",
            "is_critic",
            "is_superuser",
            "updated_at",
        ]

        read_only_fields = ["is_superuser", "updated_at"]

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="user with this email already exists.",
                    )
                ]
            },
            "username": {
                "required": True,
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ],
            },
        }


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
        ]

        read_only_fields = [
            "id",
            "first_name",
            "last_name",
        ]
