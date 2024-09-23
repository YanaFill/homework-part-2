from django.db import models

class LessonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.CharField(max_length=100)
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE)
    control = models.CharField(max_length=50, choices=[
        ('Відсутній', 'Відсутній'),
        ('Залік', 'Залік'),
        ('Іспит', 'Іспит')
    ])
    specialty = models.CharField(max_length=100)
    semester = models.IntegerField()
    image = models.ImageField(upload_to='subject_images/', blank=True, null=True)

    def __str__(self):
        return self.name
