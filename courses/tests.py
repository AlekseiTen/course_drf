from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from users.models import User
from django.shortcuts import reverse
from rest_framework import status


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="admin@kremlin.ru")
        self.course = Course.objects.create(title="Новый курс", description="Описание")
        self.lesson = Lesson.objects.create(
            title="Новый урок",
            description="Описание",
            video_url="link.youtube.com",
            course=self.course,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тест получения информации об уроке."""
        url = reverse("courses:lessons_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.lesson.title)

    def test_lesson_create(self):
        """Тест создания нового урока."""
        url = reverse("courses:lessons_create")

        # Корректные данные для создания урока
        data = {
            "title": "Урок 1",
            "course": self.course.pk,
            "description": "Описание",
            "video_url": "https://www.youtube.com/",
        }
        response = self.client.post(url, data)
        # print(response.data)
        # Проверка успешного создания
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

        # Некорректные данные для создания урока
        data = {
            "title": "Урок 1",
            "course": self.course.pk,
            "description": "Описание",
            "video_url": "https://rutube.ru/",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_lesson_update(self):
        """Тест обновления информации об уроке."""
        url = reverse("courses:lessons_update", args=(self.lesson.pk,))
        data = {"title": "Урок 2"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Урок 2")

    def test_lesson_delete(self):
        """Тест удаления урока."""
        url = reverse("courses:lessons_destroy", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        """Тест получения списка уроков для курса."""
        url = reverse("courses:lessons_list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "video_url": self.lesson.video_url,
                    "title": self.lesson.title,
                    "description": self.lesson.description,
                    "preview": None,
                    "course": self.lesson.course.pk,
                    "owner": self.lesson.owner.pk,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
