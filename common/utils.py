import json
import os
import re
from http.client import HTTPConnection, HTTPSConnection
from io import BytesIO
from urllib.parse import urlencode

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.validators import RegexValidator
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response


phone_regex = RegexValidator(regex=r'^\d{11}$', message=_('Не верный формат телефона'))
iin_regex = RegexValidator(regex=r'^[\d-]+$', message=_('ИИН может содержать только цифры'))
uid_bad_symbols = re.compile(r'[^a-zA-Z0-9]+')


def send_http_request(host, path, method='GET', body=None, secure=False):
    try:
        if secure:
            conn = HTTPSConnection(host)
        else:
            conn = HTTPConnection(host)
        conn.request(method, path, body=body)
        response = conn.getresponse()
        response_status = response.status
        response_data = response.read()
    except:
        return None
    return {
        'status': response_status,
        'data': response_data,
    }


def send_sms_code(phone, code):
    if settings.DEBUG:
        print('Sent SMS code {} for {}'.format(code, phone))
        return True

    # send_bot_message('Sent SMS code {} for {}'.format(code, phone))

    message = settings.PROJECT_TITLE + ' введите комбинацию: {}'.format(code)
    params = {
        'login': settings.SMS_ACCOUNT_NAME,
        'psw': settings.SMS_ACCOUNT_PWD,
        'phones': phone,
        'mes': message,
        'charset': 'utf-8',
        'fmt': 3,
    }

    response = send_http_request('smsc.kz', '/sys/send.php?' + urlencode(params), secure=True)
    if response is None or response['status'] != 200:
        return False

    try:
        json_data = json.loads(response['data'].decode())
    except json.decoder.JSONDecodeError:
        return False

    if 'error_code' in json_data or 'error' in json_data:
        return False

    return True


def file_delete(path):
    if path and os.path.exists(path):
        try:
            os.remove(path)
        except:
            pass


def in_dict(dic, key, default=None):
    res = None
    for k in dic:
        if isinstance(k, (list, tuple)):
            for x in k:
                if x == key:
                    res = dic[k]
                    break
            if res:
                break
        else:
            if k == key:
                res = dic[k]
                break
    return res or default


def error_response(status=400, message='', detail=None):
    data = {'error': message}
    if detail is not None:
        data['detail'] = detail
    return Response(status=status, data=data)


def error_400_response(message='', detail=None):
    return error_response(400, message, detail)


def error_401_response(message='', detail=None):
    return error_response(401, message, detail)


def error_500_response(message='', detail=None):
    return error_response(500, message, detail)


class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, error, status_code):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = {'error': error, 'detail': force_text(detail)}
        else:
            self.detail = {'error': error, 'detail': force_text(self.default_detail)}
