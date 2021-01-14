from dao.weatherbit_dao import WeatherbitDao
from entities.weatherbit import Weatherbit

class ClimaCtrl:
    api_clima = WeatherbitDao()

    def por_latitude_longitude(self, latitude, longitude):
        retorno = self.api_clima.por_latitude_longitude(latitude, longitude)
        return retorno
        #return Weatherbit(retorno)


    def por_cidade(self, cidade):
        retorno = self.api_clima.por_cidade(cidade)
        return retorno
        #return Weatherbit(retorno)