from rest_framework import serializers
from .models import Course, CourseInfo, ProgrammingLanguages, CourseSignUp



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'address')


class ProgrammingLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguages
        fields = "__all__"


class CourseInfoSerializer(serializers.ModelSerializer):
    programming_languages_id = ProgrammingLanguagesSerializer()
    course_id = CourseSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CourseInfo
        fields = ('id', 'title', 'address', 'programming_languages_id', 'price_per_month', 'total_price',
                  'description',
                  'image', 'continuance', 'course_id')

    def get_total_price(self, instance):
        return instance.price_per_month * instance.continuance


class CourseSignUpSerializer(serializers.ModelSerializer):
    price_per_month = serializers.SerializerMethodField()
    programming_languages_id = ProgrammingLanguagesSerializer

    class Meta:
        model = CourseSignUp
        fields = ("id", "user", "courseinfo_id", 'price_per_month', "date", "programming_languages_id")

    def get_price_per_month(self, instance):
        return instance.courseinfo_id.price_per_month




