from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Exam(models.Model):
    course = models.ForeignKey(
        'courses.Course',
        related_name='exams',
        on_delete=models.PROTECT,
    )
    date_time = models.DateTimeField(verbose_name='date')

    def __str__(self):
        return f'exam {self.course} ({self.date_time:%d/%m/%Y})'


class Note(models.Model):
    note = models.IntegerField(
        validators=[
            MaxValueValidator(20),
            MinValueValidator(0)
        ])
    student = models.ForeignKey(
        'persons.Student',
        related_name='notes',
        on_delete=models.PROTECT,
    )
    exam = models.ForeignKey(
        Exam,
        related_name='notes',
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = ('student', 'exam',)

    def __str__(self):
        return f'{self.student} / {self.exam} : {self.note}'
