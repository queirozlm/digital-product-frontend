from flask import Flask
import requests
import json
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/")
def pagina_inicial():
    request = requests.get("https://state-train-sp.herokuapp.com/")
    data = json.loads(request.content)
    dt = pd.json_normalize(data) 
    html = dt.to_html()
    return html

if __name__ == '__main__':
    app.run()
