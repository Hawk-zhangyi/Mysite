import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


# Create your models here.
@python_2_unicode_compatible # ������֧��python2�汾��ʱ�����Ҫ���װ����
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):  # ��python2�汾��ʹ�õ���__unique__
        return self.question_text

@python_2_unicode_compatible # ������֧��python2�汾��ʱ�����Ҫ���װ����
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text