# coding=utf-8
import unittest
from unittest.mock import patch
from parameterized import parameterized
from src import app


class TestSomething(unittest.TestCase):

	def test_check_document_existance(self):
		unittest.TestCase.setUp(self)
		self.assertEqual(app.check_document_existance('2207 876234'), True)
		unittest.TestCase.tearDown(self)
		print('Тест 1 прошёл успешно')

	@patch('src.app.input', lambda *args: '2207 876234')
	def test_get_doc_owner_name(self):
		self.assertEqual(app.get_doc_owner_name(), 'Василий Гупкин')
		print('\nТест 2 прошёл успешно')

	def test_get_all_doc_owners_names(self):
		self.assertEqual(app.get_all_doc_owners_names(), ['Василий Гупкин', 'Геннадий Покемонов', 'Иван Иванов'])
		print('Тест 3 прошёл успешно')

	def test_remove_doc_from_shelf(self):
		self.assertNotIn('2207 876234', app.remove_doc_from_shelf('2207 876234'))
		print('Тест 4 прошёл успешно')

	@parameterized.expand(
		[
			('5', ('5', True)),
			('2', ('2', False))
		]
	)
	def test_add_new_shelf(self, a, b):
		result = app.add_new_shelf(shelf_number = a)
		self.assertEqual(result, b)
		print('Тест 5 прошёл успешно')

	def test_append_doc_to_shelf(self):
		self.assertIn('123', app.append_doc_to_shelf('123', '2'))
		print('Тест 7 прошёл успешно')

	@patch('src.app.input', lambda *args: '10006')
	def test_delete_doc(self):
		self.assertEqual(app.delete_doc(), ('10006', True))
		print('Тест 8 прошёл успешно')

	@patch('src.app.input', lambda *args: '11-2')
	def test_get_doc_shell(self):
		self.assertEqual(app.get_doc_shelf(), '1')
		print('\nТест 9 прошёл успешно')

	def test_move_doc_to_shelf(self):
		self.assertEqual(app.move_doc_to_shelf('10006', '3'), f"'Документ номер 10006 был перемещен на полку номер 3")
		print('Тест 10 прошёл успешно')

	def test_show_document_info(self):
		self.assertEqual(app.show_document_info(app.documents[0]), 'passport 2207 876234 Василий Гупкин')
		print('Тест 11 прошёл успешно')

	def test_show_all_docs_info(self):
		self.assertEqual(app.show_all_docs_info(), ['passport 2207 876234 Василий Гупкин',
		                                            'invoice 11-2 Геннадий Покемонов',
		                                            'passport 123456 Иван Иванов'])
		print('Тест 12 прошёл успешно')

	def test_add_new_doc(self):
		self.assertEqual(app.add_new_doc('123456', 'passport', 'Иван Иванов', '3'), {"type": 'passport',
		                                                                             "number": '123456',
		                                                                             "name": 'Иван Иванов'})
		print('Тест 13 прошёл успешно')

	@patch('src.app.input', lambda *args: '11-2')
	def test_secretary_program_start_p(self):
		self.assertEqual(app.secretary_program_start('p'), 'Владелец документа - Геннадий Покемонов')

	def test_secretary_program_start_ap(self):
		self.assertEqual(app.secretary_program_start('ap'), ("Список владельцев документов - ['Василий Гупкин', 'Геннадий Покемонов', "
 "'Иван Иванов']"))


if __name__ == '__main__':
	unittest.main()