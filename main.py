from flask import Flask
from api import api
from flask_cors import CORS
from sample_site import site

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)
app.register_blueprint(site)
