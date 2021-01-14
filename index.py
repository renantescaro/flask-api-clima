from flask import Flask
from flask_caching import Cache
from controller.clima_ctrl import ClimaCtrl

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)

climaCtrl = ClimaCtrl()

@app.route("/")
@app.cache.cached(timeout=300)
def por_latitude_longitude():
    return climaCtrl.por_latitude_longitude(123,321)

@app.route("/cidade")
@app.cache.cached(timeout=300)
def por_cidade():
    return climaCtrl.por_cidade('penapolis')

app.run(port=5000, debug=True, host='0.0.0.0')