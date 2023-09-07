from flask import Flask, render_template,jsonify,request
import numpy as np
from joblib import load
import os

#Cargar el modelo
dt=load("dt1.joblib")

#Generar el servidor (backend)
servidorWeb = Flask(__name__)

@servidorWeb.route("/holamundo", methods=['GET'])
def holamundo():
        return render_template('pagina1.html')

#Envio de datos a traves de JSON        
@servidorWeb.route('/modelo',methods=['POST'])        
def modeloPrediccion():
        #procesar los deatos de entrada
        contenido=request.json
        print(contenido)
        datosEntrada = np.array([
                0.88,	0,	2.6,	0.098,	25,	67,	0.9968,
                contenido['pH'],
                contenido['sulphates'],
                contenido['alcohol']
        ])
        #utiizar el modelo
        resultado=dt.predict(datosEntrada.reshape(1,-1))

        return jsonify({'resultado':str(resultado[0])})


if __name__ == '__main__':
        servidorWeb.run(debug=False,host='0.0.0.0',port='8080')