from dao.api import Api

class WeatherbitDao:

    def __init__(self):
        self.url_api = 'http://api.weatherbit.io/v2.0/current'
        self.url_img = '/assets/imagens/'
        self.ext_img = '.png'
        self._key    = '7b6aa93b6f924b51ba2860da2e0142a1'
        self._api    = Api(self.url_api)

    def por_latitude_longitude(self, latitude, longitude):
        self._response = self._api.get(parametros={'lat':latitude, 'lon':longitude, 'key':self._key, 'lang':'pt'})
        self.setar_imagem_clima()
        return self._response

    def por_cidade(self, cidade, pais):
        self._response = self._api.get(parametros={'city':cidade, 'country':pais, 'key':self._key, 'lang':'pt'})
        self.setar_imagem_clima()
        return self._response

    def setar_imagem_clima(self):
        response_json = self._response.json()
        response_json['data'][0]['weather_image'] = self.obter_url_imagem()
        self._response = str(response_json)

    def obter_url_imagem(self):
        return (str(self.url_img) + str(self.imagem_api()) + str(self.ext_img))

    def imagem_api(self):
        response_json = self._response.json()
        return response_json['data'][0]['weather']['icon']
        
    