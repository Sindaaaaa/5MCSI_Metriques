from flask import Flask, rendertemplatestring, rendertemplate, jsonify
from flask import rendertemplate
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3

app = Flask(name)

@app.route('/')
def hello_world():
    return render_template('hello.html') #comm2

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("forms.html")

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme/")
def colonnes():
    return render_template("colonnes.html")


if __name == "__main":
  app.run(debug=True)
