# from rest_framework.views import exception_handler
from rest_framework import exceptions
from django.http import Http404
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from django.db import connection, transaction
from django.db import DatabaseError


def customExceptionHandler(exc, context):
    """
    重写rest_framework.views.exception_handler
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    # 接口异常
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            if isinstance(exc.detail, list):
                errors = exc.detail
            else:
                errors = {k: v[0] for k, v in exc.detail.items()}
        else:
            errors = exc.detail

        set_rollback()
        data = {'code': -1, 'msg': '失败', 'errors': errors, 'data': []}
        return Response(data, status=exc.status_code, headers=headers)

    # 如果是数据库异常
    if isinstance(exc, DatabaseError):
        errors = '数据库异常，请联系管理员'
        data = {'code': -2, 'msg': '失败', 'errors': errors, 'data': []}
        return Response(data)

    return None


def set_rollback():
    atomic_requests = connection.settings_dict.get('ATOMIC_REQUESTS', False)
    if atomic_requests and connection.in_atomic_block:
        transaction.set_rollback(True)
