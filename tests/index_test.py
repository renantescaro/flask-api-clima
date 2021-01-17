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

    def test_content(self):
            response_str = self.response.data.decode('utf-8')
            self.assertIn('"chuva":', str(response_str), msg='Erro retorno sem chave "chuva"')
            self.assertIn('"data":', str(response_str), msg='Erro retorno sem chave "data"')
            self.assertIn('"endereco":', str(response_str), msg='Erro retorno sem chave "endereco"')
            self.assertIn('"temperatura":', str(response_str), msg='Erro retorno sem chave "temperatura"')
            self.assertIn('"umidade":', str(response_str), msg='Erro retorno sem chave "umidade"')
            self.assertIn('"urlImagem":', str(response_str), msg='Erro retorno sem chave "urlImagem"')
            self.assertIn('"vento":', str(response_str), msg='Erro retorno sem chave "vento"')

if __name__ == '__main__':
    unittest.main()