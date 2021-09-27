from flask import Flask
from flask import Flask, render_template, request
import pickle
import sklearn
import numpy as np

app = Flask(__name__)
try:
    model = pickle.load(open('crop_recommendation.pkl', 'rb'))
except FileNotFoundError as e:
    print(e)

@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def prediction():
    if request.method == 'POST':
        n = float(request.form['n'])
        p = float(request.form['p'])
        k = float(request.form['k'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        output = model.predict([[n, p, k, temperature, humidity, ph, rainfall]])

        res = ""
        if output==18:
            res="Pigeonpeas "
        if output==11:
            res="Maize"
        if output==3:
            res="Chickpea"
        if output==9:
            res="Kidneybeans"
        if output==20:
            res="Rice"
        if output==13:
            res="Mothbeans"
        if output==14:
            res="Mungbean"
        if output==2:
            res="Blackgram"
        if output==10:
            res="Lentil"
        if output==19:
            res="Pomegranate"
        if output==1:
            res="Banana"
        if output==12:
            res="Mango"
        if output==7:
            res="Grapes"
        if output==21:
            res="Watermelon"
        if output==15:
            res="Muskmelon"
        if output==0:
            res="Apple"
        if output==16:
            res="Orange"
        if output==17:
            res="Papaya"
        if output==4:
            res="Coconut"
        if output==6:
            res="Cotton"
        if output==8:
            res="Jute"
        if output==5:
            res="Coffee"
        #else:
            #res="Unable to predict"
        return render_template('Prediction.html',predict_res= res)


@app.route("/result" ,  methods=['GET'])
def result():
    pass


if __name__ == "__main__":
    app.debug = True
    app.run()
