from django.urls import path
from rest_framework.routers import SimpleRouter

from courses.apps import CoursesConfig
from courses.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonDestroyApiView,
    LessonListApiView,
    LessonRetrieveApiView,
    LessonUpdateApiView,
    SubscriptionView,
)

app_name = CoursesConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lessons_list"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lessons_retrieve"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lessons_create"),
    path(
        "lessons/<int:pk>/destroy/",
        LessonDestroyApiView.as_view(),
        name="lessons_destroy",
    ),
    path(
        "lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lessons_update"
    ),
    path(
        "<int:course_id>/subscribe/", SubscriptionView.as_view(), name="subscribe_view"
    ),
]

urlpatterns += router.urls
