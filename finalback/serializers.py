from django.contrib.auth.models import User
from rest_framework import serializers, validators

from finalback.models import role


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name",)
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "هذا الأسم مستخدم الرجاء إدخال أسم جديد"
                    )
                ],
            },
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            # role=validated_data["role"],
            # email=validated_data["email"],
            # first_name=validated_data["first_name"],
            # last_name=validated_data["last_name"]
        )
        return user



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = '__all__'