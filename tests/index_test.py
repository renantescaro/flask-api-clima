import sys
sys.path.append('c:/xampp/htdocs/python/flask-api-clima/')

import unittest
from index import app


class IndexTest(unittest.TestCase):
    def setUp(self):
        api = app.test_client()
        self.response = api.get('cidade/Penápolis/BR')

    def test_get(self):
        self.assertEqual(200, self.response.status_code, msg='Erro status code')

    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type, msg='Erro content type')

if __name__ == '__main__':
    unittest.main()