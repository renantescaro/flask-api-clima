from dao.weatherbit_dao import WeatherbitDao

class ClimaCtrl:
    api_clima = WeatherbitDao()

    def por_latitude_longitude(self, latitude, longitude):
        return self.api_clima.por_latitude_longitude(latitude, longitude)

    def por_cidade(self, cidade, pais):
        return self.api_clima.por_cidade(cidade, pais)