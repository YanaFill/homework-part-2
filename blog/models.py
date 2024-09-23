from django.db import models
from django.utils import timezone


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = ('DF', 'Draft')
        PUBLISHED = ('PB', 'Published')

    title = models.CharField(verbose_name="Назва поста", max_length=20)
    body = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} - {self.pk}"

    class Meta:
        ordering = ["-publish"]


class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title
