from rest_framework.serializers import ModelSerializer, SerializerMethodField

from courses.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    """Для курса добавил поле количество уроков"""

    lessons_count = SerializerMethodField()

    def get_lessons_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ("id", "title", "lessons_count")


class CourseDetailSerializer(ModelSerializer):
    """выводит информацию о курсе и связанную информацию о его уроках"""

    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, course):
        return course.lessons.count()

    class Meta:
        model = Course
        fields = ("title", "lessons_count", "lessons")
