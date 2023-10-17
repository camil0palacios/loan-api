from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app);

# Set up
from .libs.core import setup
