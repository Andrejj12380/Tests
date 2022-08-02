# coding=utf-8
from parameterized import parameterized
import unittest
from yandex import uploader
from unittest import TestCase
import requests


class TestYaAPI(TestCase):

	@parameterized.expand(
		[
			('test', 200),
			('tes', 404)
		]
	)
	def test_folder_create(self, a, b):
		try:
			uploader.folder_create('test')
		except requests.exceptions.HTTPError:
			print('Папка уже существует')
		response = uploader.get_resource_info(a)
		template = b
		self.assertEqual(response, template)


if __name__ == '__main__':
	unittest.main()