from flask import jsonify, make_response
import requests
import json

class Api:
    def __init__(self, url):
        self._url = url

    def get(self, parametros):
        r = requests.get(url=self._url, params=parametros)
        r.headers["Content-Type"] = "application/json"
        return r.text