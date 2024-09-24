from django.contrib.auth.models import User
from django.db import models

class LessonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField('Назва предмету', max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    teacher = models.CharField('Викладач', max_length=100)
    lesson_type = models.ForeignKey(verbose_name='Тип заняття', to=LessonType, on_delete=models.CASCADE)
    control = models.CharField('Контроль', max_length=50, choices=[
        ('Відсутній', 'Відсутній'),
        ('Залік', 'Залік'),
        ('Іспит', 'Іспит')
    ])
    specialty = models.CharField('Спеціальність', max_length=100)
    semester = models.IntegerField('Семестр')
    image = models.ImageField('Зображення', upload_to='subject_images/', blank=True, null=True)

    def __str__(self):
        return self.name
