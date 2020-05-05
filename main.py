from flask import Flask
from api import api
from sample_site import site

app = Flask(__name__)

app.register_blueprint(api)
app.register_blueprint(site)
