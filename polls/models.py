from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Option(models.Model):
    option = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.option
