#!/usr/local/bin/python
# coding: utf-8
import urllib
import urllib.request

import request_constants


# Вызов транспортных запросов МИВ
def url_register_request():
    """регистрируем url для приема справочнка п2.6.3.2 из спецификации МИВ"""

    headers = {
        'Host': '0.0.0.0:8860'  # ???
        , 'Content-Type': 'multipart/form-data; boundary=FAKE-BOUNDARY'
        , 'Accept': '*/*'
        , 'Content-Length': str(len(request_constants.RESPONSE_URL))
    }

    data = "--FAKE-BOUNDARY" \
           "Content-Disposition: form-data; name=\"receive\"" \
           "{0}" \
           "--FAKE-BOUNDARY".format(request_constants.RESPONSE_URL)

    responce = ""
    error = ""
    try:
        request = urllib.request.Request(request_constants.MIV_URL, str.encode(data), headers)
        responce = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        error = e.reason

    return responce, error


def miv_request(data_xml):
    """регистрируем url для приема справочнка п2.6.3.2 из спецификации МИВ"""

    headers = {
        'Host': '0.0.0.0:8860'  # ???
        , 'Content-Type': 'multipart/form-data; boundary=FAKE-BOUNDARY'
        , 'Accept': '*/*'
        , 'Content-Length': str(len(data_xml))
    }

    # Значит это запрос на регистрацию

    data = "--FAKE-BOUNDARY" \
           "Content-Disposition: form-data; name=\"receive\"" \
           "{0}" \
           "--FAKE-BOUNDARY".format(data_xml)

    responce = ""
    error = ""
    try:
        request = urllib.request.Request(request_constants.MIV_URL, str.encode(data), headers)
        responce = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        error = e.reason

    return responce, error
