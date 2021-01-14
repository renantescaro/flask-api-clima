class Api:
    def __init__(self, url):
        self._url = url

    def get(self, endpoint):
        return str(self._url) + str(endpoint)