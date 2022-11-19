import os

from flask import Flask

from views import bp_main

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")



app = Flask(__name__)
app.register_blueprint(bp_main)

app.run(port=25000)
