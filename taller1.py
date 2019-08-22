from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app= Flask(__name__)
CORS(app)

tipo_medicion={'sensor':'DS18B20','variable':'TEMPERATURA DE AMBIENTE', 'unidades':'Centigrados , Fahrenheit'}

mediciones = [
  {'Fecha': '2019-01-29 12:39:37', **tipo_medicion, 'valor':28},
  {'Fecha': '2019-02-20 14:30:41', **tipo_medicion, 'valor':27},
  {'Fecha': '2019-04-14 18:45:21', **tipo_medicion, 'valor':20},
  {'Fecha': '2019-05-10 18:45:21', **tipo_medicion, 'valor':24},
  {'Fecha': '2019-06-15 18:45:21', **tipo_medicion, 'valor':29},
  {'Fecha': '2019-07-28 18:45:21', **tipo_medicion, 'valor':18}
]

@app.route('/mediciones', methods=['POST'])
def postOne():
    now = datetime.now()
    body = request.json
    body['Fecha'] = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    mediciones.append({**body, **tipo_medicion})
    return jsonify(mediciones)

@app.route('/')
def get():
    return jsonify(tipo_medicion)

@app.route('/mediciones', methods=['GET'])
def getAll():
    return jsonify(mediciones)

@app.route('/mediciones/Fecha/<string:Fecha>',methods=['GET'])
def getMayoresA(Fecha):
    variable=[]
    for medicion in mediciones:
        if medicion['Fecha']>Fecha: 
            variable+={medicion['Fecha'] ,medicion['valor']}
    return jsonify(variable)

@app.route('/mediciones/valor/<int:valor>',methods=['GET'])
def getMayoresB(valor):
    suma=[]
    for medicion in mediciones:
        if medicion['valor']>valor: 
            suma+={medicion['Fecha'] ,medicion['valor']}
    return jsonify(suma)

app.run(port=5000 , debug= True)

