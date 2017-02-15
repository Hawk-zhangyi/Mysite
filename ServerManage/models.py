from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from pip.cmdoptions import verbose


# Create your models here.

@python_2_unicode_compatible # ������֧��python2�汾��ʱ�����Ҫ���װ����
class ServerInfo(models.Model):
    class Meta:         #define show name
        verbose_name = '服务器'
        verbose_name_plural = '服务器'
        
    Server_Name = models.CharField('机器名',max_length=200)
    Server_IP = models.CharField('IP地址',max_length=15)
    create_date = models.DateTimeField('创建时间')
    state = models.CharField('状态',max_length=2)
    def __str__(self):  # ��python2�汾��ʹ�õ���__unique__
        return self.Server_Name
    