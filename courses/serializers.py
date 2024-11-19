from rest_framework import serializers

from courses.models import Course, Lesson
from courses.validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    # Для уроков добавил валидатор только на ютуб
    video_url = serializers.CharField(validators=[validate_youtube_link])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """Для курса добавил поле количество уроков"""

    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ("id", "title", "lessons_count")


class CourseDetailSerializer(serializers.ModelSerializer):
    """выводит информацию о курсе и связанную информацию о его уроках"""

    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ("title", "lessons_count", "lessons")
