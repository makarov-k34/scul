#!/usr/local/bin/python
# coding: utf-8
import miv_api

import xml.etree.ElementTree as ET
import request_constants
import urllib

from urllib import request


def url_register_request():
    """регистрируем url для приема справочнка п2.6.3.2 из спецификации МИВ"""

    response, err = miv_api.url_register_request()

def get_IHI_sceleton():
    """Отправляет GET-запрос для получения каркаса-XML-запроса. Метапакет отдается синхронно!"""

    response = ""
    error = None
    try:
        responce = request.urlopen(request_constants.IHI_GET_SKELETON_URL).read().decode('utf-8')
    except urllib.error.URLError as e:
        error = e.reason

    return response, error


def GetClassifierRequestXMLRest(xml):
    """получение классификатора(обьекта), одного конкретного"""
    response = ""
    err = None

    ihi_xml_skeleton = request.urlopen(request_constants.IHI_GET_SKELETON_URL).read().decode('utf-8')

    XML_request = ET.fromstring(ihi_xml_skeleton)

    try:
        for codeBlock in XML_request.iter('Codeblock'):
            codeBlock.set('language', request_constants.KATIA_METADATAQUERY)

        for publicCode in XML_request.iter('PublicCode'):
            publicCode.text = "<![CDATA[{0}]]>".format(xml)
    except:
        print('')

    request_data = ET.tostring(XML_request, encoding='utf8', method='xml')
    response, err = miv_api.miv_request(request_data)

    #WriteTofile("classifier.txt", response) #no access anyway on testmachine 

    return response, err


def GetClassifierRequestSQL(ihi_xml_skeleton, sql_string):
    """получение классификатора(обьекта), одного конкретного"""
    response = ""
    err = None

    XML_request = ET.fromstring(ihi_xml_skeleton)

    try:
        for codeBlock in XML_request.iter('CodeBlock'):
            codeBlock.set('language', request_constants.PL_SLQ)

        for publicCode in XML_request.iter('PublicCode'):
            publicCode.text = "<![CDATA[{0}]]>".format(sql_string)
    except:
        print('')
    request_data = ET.tostring(XML_request, encoding='utf8', method='xml')
    response, err = miv_api.miv_request(request_data)
    WriteTofile("classifier.txt", response)
    return response, err

def GetClassifiersList(ihi_xml_sceleton):
    """получение списка классификаторов"""
    pass

def WriteTofile(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
        f.close()
