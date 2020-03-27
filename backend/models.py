from django.db import models

# Create your models here.


class ApiGroup(models.Model):
    projId = models.IntegerField('项目id', null=False, unique=True)
    apiGroupJson = models.CharField(
        '接口分组信息', null=False, max_length=4096, default='[{"id":1,"apiGroupName":"默认分组","isEdit":0}]')

    class Meta:
        verbose_name = '接口分组表'
