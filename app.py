import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model = load("project.save")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():

    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    d = request.form['d']
    e = request.form['e']
    f= request.form['f']
    g= request.form['g']
    
    total = [[a,b,c,d,e,f,g]]
    total_1 = np.asarray(total, dtype='float64')
    #print(total_1)
    prediction = model.predict(total_1)
    output = np.round(prediction[0][0], 2)
    #print(prediction)
    #output=prediction[0][0]
    
    return render_template('index.html', prediction_text='Chance of Admit {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
