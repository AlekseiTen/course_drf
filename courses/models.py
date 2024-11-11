from django.db import models


NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    preview = models.ImageField(
        upload_to="course/previews/", verbose_name="Фото", **NULLABLE
    )
    description = models.TextField(
        verbose_name="Описание курса", **NULLABLE, help_text="Укажите описание курса"
    )
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Укажите владельца курса"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Название курса",
        related_name="lessons",
        **NULLABLE
    )
    title = models.CharField(max_length=200, verbose_name="Название урока")
    description = models.TextField(verbose_name="Описание урока", **NULLABLE)
    preview = models.ImageField(
        upload_to="lesson/previews/", verbose_name="Фото", **NULLABLE
    )
    video_url = models.URLField(verbose_name="Ссылка на видео", **NULLABLE)
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Укажите владельца урока"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
