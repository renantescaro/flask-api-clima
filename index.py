from flask import Flask, jsonify, url_for, send_file
from flask_caching import Cache
from controller.clima_ctrl import ClimaCtrl
from flask_cors import CORS

app = Flask('api_clima', static_url_path='/static', static_folder='static')
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

#@app.cache.cached(timeout=300)
@app.route('/img/<imagem>', methods=['GET'])
def imagem(imagem):
    return send_file('static/images/'+str(imagem), mimetype='image/PNG')

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')