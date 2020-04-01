from django.db import models

# Create your models here.


class ApiGroup(models.Model):
    projId = models.IntegerField('项目id', null=False, unique=True)
    apiGroupJson = models.CharField(
        '接口分组信息', null=False, max_length=4096,
        default='[{"id":1,"apiGroupName":"默认分组","isEdit":0}]')

    class Meta:
        verbose_name = '接口分组表'


class Apis(models.Model):
    projId = models.IntegerField('项目id', null=False)
    apiGroupId = models.IntegerField('接口分组id', null=False)
    apiSortNo = models.IntegerField('接口排序号', null=False)
    apiName = models.CharField('接口名称', null=False, max_length=64)
    apiPath = models.CharField('接口地址', null=False, max_length=64, default='')
    apiProtocol = models.CharField(
        '请求协议，http/https', null=False, max_length=8, default='http')
    apiMethod = models.CharField('请求类型， GET/POST', null=False, max_length=8)
    apiHeaders = models.CharField(
        '请求头部信息，json格式', max_length=4096, default='[]')
    apiQuerys = models.CharField(
        '请求参数信息，json格式', max_length=4096, default='[]')
    apiBody = models.CharField(
        '请求body信息，json格式', max_length=4096, default='[]')
    apiResp = models.CharField(
        '请求返回信息示例，json格式', max_length=4096, default='[]')

    class Meta:
        verbose_name = '接口表'
        # 同项目同一分组下 接口名称唯一
        unique_together = (("projId", "apiGroupId", "apiName"))
