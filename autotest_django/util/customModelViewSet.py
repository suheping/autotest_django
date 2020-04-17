
from rest_framework import viewsets
from rest_framework.response import Response


class ReturnMsg:
    def __init__(self, code=1, msg='成功', errors=None, data=None):
        self.code = code
        self.msg = msg
        self.errors = {} if errors is None else errors
        self.data = [] if data is None else data

    def dict(self):
        return {
            'code': self.code,
            'msg': self.msg,
            'errors': self.errors,
            'data': self.data
        }


class CustomModelViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(),
                        status=response.status_code)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(),
                        status=response.status_code)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(),
                        status=response.status_code)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(),
                        status=response.status_code)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(),
                        status=response.status_code)

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(),
                        status=response.status_code)
