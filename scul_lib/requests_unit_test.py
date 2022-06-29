#!/usr/local/bin/python
# coding: utf-8
import unittest

import request_constants

import scul_api

class MyTest(unittest.TestCase):
	def test_get_IHI_sceleton_test(self):
		response, err=scul_api.get_IHI_sceleton()
		print("SCELETON RESPONSE::"+response) #.decode('utf-8')
		#print("error:"+str(error))
		self.assertEqual(err, None)


	def test_get_IHI_classifier_XML(self):

		classifier_response, err=scul_api.GetClassifierRequestXMLRest(request_constants.IHI_REQUEST_FORDATA_XML)
		print("BATCH response:"+classifier_response)
		self.assertEqual(err, None)

