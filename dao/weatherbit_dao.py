from dao.api import Api
from entities.converter import Converter
import json

class WeatherbitDao:

    def __init__(self):
        self.url_api = 'http://api.weatherbit.io/v2.0/current'
        self.caminho_imagens = '/img/'
        self.extensao_imagem = '.png'
        self._key = '7b6aa93b6f924b51ba2860da2e0142a1'
        self._api = Api(self.url_api)
        self._json_final = {}

    def por_latitude_longitude(self, latitude, longitude):
        self._response = self._api.get(parametros={'lat':latitude, 'lon':longitude, 'key':self._key, 'lang':'pt'})
        self.setar_dados()
        return self._json_final

    def por_cidade(self, cidade, pais):
        self._response = self._api.get(parametros={'city':cidade, 'country':pais, 'key':self._key, 'lang':'pt'})
        self.setar_dados()
        return self._json_final

    def setar_dados(self):
        converter = Converter()
        response_json = self._response.json()
        self._json_final = {
            "endereco"   : self.obter_endereco(),
            "data"       : converter.data_atual_string(),
            "urlImagem"  : self.obter_url_imagem(),
            "temperatura": response_json['data'][0]['temp'],
            "clima"      : response_json['data'][0]['weather']['description'],
            "umidade"    : round(response_json['data'][0]['rh'],2),
            "vento"      : round( converter.ms_para_kh(response_json['data'][0]['wind_spd']),2)
        }

    def obter_endereco(self):
        response_json = self._response.json()
        return (str(response_json['data'][0]['city_name']) +
                ' / ' +
                str(response_json['data'][0]['country_code']))

    def obter_url_imagem(self):
        response_json = self._response.json()
        nome_imagem   = response_json['data'][0]['weather']['icon']
        return (str(self.caminho_imagens) + str(nome_imagem) + str(self.extensao_imagem))