from flask import Flask, jsonify
from flask_caching import Cache
from controller.clima_ctrl import ClimaCtrl
from flask_cors import CORS

app = Flask(__name__, static_url_path='/assets/imagens/', static_folder='/assets/imagens/')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)
CORS(app)

climaCtrl = ClimaCtrl()

@app.route('/posicao/<lat>/<lon>', methods=['GET'])
@app.cache.cached(timeout=300)
def por_latitude_longitude(lat, lon):
    return jsonify(climaCtrl.por_latitude_longitude(lat, lon))

@app.route('/cidade/<cidade>/<pais>', methods=['GET'])
@app.cache.cached(timeout=300)
def por_cidade(cidade, pais):
    return jsonify(climaCtrl.por_cidade(cidade, pais))

app.run(port=5000, debug=True, host='0.0.0.0')