from django.http import HttpResponse
import json
import urllib
from backend.models import ApiGroup

# 首页


def index(request):
    return HttpResponse("hello")


def getApiGroup(request, projId):
    # 返回的的是dict
    apiGroupRes = ApiGroup.objects.filter(
        projId=projId).values('apiGroupJson').first()
    # 取到dict中apiGroupJson字段的值，并且把'替换为"
    # apiGroupStr为str
    apiGroupStr = apiGroupRes['apiGroupJson'].replace("'", '"')
    print(apiGroupStr)
    # 将apiGroupStr从str转为dict，保存为apiGroupDict
    apiGroupDict = json.loads(apiGroupStr)
    print(apiGroupDict)
    # 将apiGroupDict从dict转为json格式的字符串
    apiGroupJson = json.dumps(apiGroupDict, ensure_ascii=False)
    return HttpResponse(apiGroupJson, content_type="application/json")


def updateApiGroup(request, projId):
    if request.method == 'POST':
        # request.body 为bytes，需要转为str并且将unicode转为utf8
        apiGroupStr = str(request.body, encoding="utf-8")
        apiGroupDict = json.loads(apiGroupStr)
        ApiGroup.objects.filter(projId=projId).update(
            apiGroupJson=apiGroupDict)
        res = [{'code': 1000, 'msg': 'success'}]
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type="application/json")
