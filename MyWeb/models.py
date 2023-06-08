from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField('date')

    def __str__(self):
        return self.name


class grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade_name = models.CharField(max_length=100)
    grade_score = models.FloatField(default=0)

    def __str__(self):
        return self.grade_name