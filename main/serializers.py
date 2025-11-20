from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import (
    Course,
    Teacher,
    Partner,
    BannerImage,
    CourseDescription,
    CourseIcon,
    CourseDescriptionGroup,
    FAQ,
)


class CourseDescriptionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDescriptionGroup
        fields = "__all__"


class CourseDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDescription
        fields = "__all__"


class CourseIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseIcon
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    icons = CourseIconSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    descriptions = serializers.SerializerMethodField()
    icons = CourseIconSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_descriptions(self, obj):
        description_groups = obj.description_groups.all()
        result = []
        for group in description_groups:
            descriptions = CourseDescriptionSerializer(
                group.descriptions.all(), many=True
            ).data
            result.append({"title": group.title, "descriptions": descriptions})

        return result


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Username yoki parol noto‘g‘ri!")
        data["user"] = user
        return data


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"
