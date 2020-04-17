from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
import urllib
from backend.models import ApiGroup, Apis
from django.forms.models import model_to_dict
from backend.serializers import ApiGroupSerializer

# 首页


def index(request):
    return HttpResponse("hello")


def getApiGroup(request, projId):
    '''获取接口分组
    '''
    # 返回的的是dict
    apiGroupRes = ApiGroup.objects.filter(
        projId=projId).values('apiGroupJson').first()
    # apiGroupRes = ApiGroup.objects.get(projId=projId)
    # print(apiGroupRes)
    # print(type(apiGroupRes))
    # 取到dict中apiGroupJson字段的值，并且把'替换为"
    # apiGroupStr为str
    apiGroupStr = apiGroupRes['apiGroupJson'].replace("'", '"')
    print(apiGroupStr)
    # 将apiGroupStr从str转为dict，保存为apiGroupDict
    apiGroupDict = json.loads(apiGroupStr)
    print(apiGroupDict)
    # 将apiGroupDict从dict转为json格式的字符串
    apiGroupJson = json.dumps(apiGroupDict, ensure_ascii=False)
    print(apiGroupJson)
    print(type(apiGroupJson))
    return HttpResponse(apiGroupJson, content_type="application/json")


def updateApiGroup(request, projId):
    '''更新接口分组
    '''
    if request.method == 'POST':
        # request.body 为bytes，需要转为str并且将unicode转为utf8
        apiGroupStr = str(request.body, encoding="utf-8")
        apiGroupDict = json.loads(apiGroupStr)
        ApiGroup.objects.filter(projId=projId).update(
            apiGroupJson=apiGroupDict)
        res = [{'code': 1000, 'msg': 'success'}]
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")


def getApi(request, projId, apiGroupId):
    '''获取接口分组下的接口
    '''
    # 返回QuerySet对象，多条记录
    # apisRes = Apis.objects.filter(
    #     projId=projId, apiGroupId=apiGroupId).values()
    apisRes = Apis.objects.filter(
        projId=projId, apiGroupId=apiGroupId).order_by('apiSortNo').values()
    # print(apisRes)
    # QuerySet对象转为list
    apisList = list(apisRes)
    # print(apisList)
    # print(apisList)
    # list转为str
    # '替换为"，再去掉{}两侧的"，再去掉[]两侧的"
    apisStr = str(apisList).replace("'", '"').replace(
        '"{', '{').replace('}"', '}').replace('"[', '[').replace(']"', ']')
    # print('apisStr', apisStr)
    # str转为dict
    apisDict = json.loads(apisStr)
    # apisDict = eval(apisStr)
    # print('apisDict', apisDict)
    # dict转为json
    apisJson = json.dumps(apisDict, ensure_ascii=False)
    print('获取接口：apisJson', apisJson)
    return HttpResponse(apisJson, content_type="application/json")


def updateApi(request):
    if request.method == 'POST':
        # body为bytes，转为str
        apisStr = str(request.body, encoding='utf-8')
        # str转为dict
        apisDict = eval(apisStr)
        print('更新接口：apisDict', apisDict)
        for i in apisDict:
            Apis.objects.filter(id=i['id']).update(**i)
        res = [{'code': 1000, 'msg': 'success'}]
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")


def addApi(request):
    if request.method == 'POST':
        apiStr = str(request.body, encoding='utf-8')
        apiDict = eval(apiStr.replace('\\n', ''))
        print('新增接口：apiDict', apiDict)
        # 入库
        Apis.objects.create(**apiDict)
        res = [{'code': 1000, 'msg': 'success'}]
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")
