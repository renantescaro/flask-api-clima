from dao.api import Api

class WeatherbitDao:
    api = Api('http://api.weatherbit.io/v2.0/current')
    key = '7b6aa93b6f924b51ba2860da2e0142a1'

    def por_latitude_longitude(self, latitude, longitude):
        return self.api.get(parametros={'lat':latitude, 'lon':longitude, 'key':self.key, 'lang':'pt'})

    def por_cidade(self, cidade, pais):
        return self.api.get(parametros={'city':cidade, 'country':pais, 'key':self.key, 'lang':'pt'})