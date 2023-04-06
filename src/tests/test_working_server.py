import unittest
import requests

class Test_Working_Server(unittest.TestCase):

    def test_root_url(self):
        url = 'http://localhost:8000'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)






