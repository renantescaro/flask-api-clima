from dao.api import Api

class WeatherbitDao:
    api = Api('http://api.weatherbit.io/v2.0/current')

    def por_latitude_longitude(self, latitude, longitude):
        return self.api.get('?lat=123&lon=3453&key=7b6aa93b6f924b51ba2860da2e0142a1')

    def por_cidade(self, cidade):
        return self.api.get('')