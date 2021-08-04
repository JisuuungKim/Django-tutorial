import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # @admin.display(
    #     boolean=True,
    #     ordering='pub_date',
    #     description='Published recently?',
    # )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #Question이라는 데이터 모델을 question이 참고함 => ForeignKey 때문
    #CASCADE => Question이 삭제되면 question도 삭제된다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

#하나의 Question에 여러개의 Choice를 다루므로 일대다 관계