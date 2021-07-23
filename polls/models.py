import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # (현재시각 - 하루전날 시각 = 어제 시각) 어제 이후에 발행된 데이터 리턴

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #Question이라는 데이터 모델을 question이 참고함 => ForeignKey 때문
    #CASCADE => Question이 삭제되면 question도 삭제된다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

#하나의 Question에 여러개의 Choice를 다루므로 일대다 관계