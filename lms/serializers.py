from rest_framework import serializers

from lms.models import Lesson, Course
from lms.validators import URLValidator
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(field='video_url')]


class SubscribeSerializer(serializers.ModelSerializer):
    sign_of_subscription = serializers.SerializerMethodField()

    def get_sign_of_subscription(self, instance):
        if instance.user.subscribe.courses in instance.subscribe_set:
            return "Yes"
        return "None"

    class Meta:
        model = Course
        fields = 'proprietor'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    sign_of_subscription = serializers.SerializerMethodField()
    lessons_list = LessonSerializer(source='lessons', many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lessons.all().count()


    def get_sign_of_subscription(self, instance):
        print(instance.proprietor.subscribe)
        if instance == instance.proprietor.subscribe:
            return "Yes"
        return "None"
