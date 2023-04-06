import unittest
from src.server.load_page import load_page_from_get_request

class Test_Load_Page(unittest.TestCase):
    def test_find_file_index(self):
        request_data = 'GET / HTTP/1.1'
        response = load_page_from_get_request(request_data).decode('utf-8')
        result = response.split(' ')[1]

        self.assertEqual(result, 200)