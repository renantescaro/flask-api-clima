from flask import Flask
from flask_caching import Cache
from controller.clima_ctrl import ClimaCtrl

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)

climaCtrl = ClimaCtrl()

@app.route('/posicao/<lat>/<lon>', methods=['GET'])
@app.cache.cached(timeout=300)
def por_latitude_longitude(lat, lon):
    return climaCtrl.por_latitude_longitude(lat, lon)

@app.route('/cidade/<cidade>/<pais>', methods=['GET'])
@app.cache.cached(timeout=300)
def por_cidade(cidade, pais):
    return climaCtrl.por_cidade(cidade, pais)

app.run(port=5000, debug=True, host='0.0.0.0')