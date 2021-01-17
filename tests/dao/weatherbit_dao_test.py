import sys
sys.path.append('c:/xampp/htdocs/python/flask-api-clima/')

import unittest
from index import app
from dao.weatherbit_dao import WeatherbitDao


class WeatherbitDaoTest(unittest.TestCase):
    def por_latitude_longitude_test(self):
        pass

if __name__ == '__main__':
    unittest.main()