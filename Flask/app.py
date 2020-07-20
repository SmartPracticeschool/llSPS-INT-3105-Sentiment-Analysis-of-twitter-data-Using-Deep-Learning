
import os
from flask import Flask, request, jsonify, render_template
from brain import brain

app = Flask(__name__)
@app.route('/')
def home():
    err = "Saved Model Doesn't Exist"
    if os.path.isfile('./model.h5'): err = ''
    return render_template('Sentimental analysis.html', result = 'https://i.pinimg.com/originals/35/db/8f/35db8f2d7d1b7734c27c3938c672d7a4.png', err = err)
@app.route('/',methods=['POST'])
def y_predict():
    sentiment = request.form["Message"]
    err, res = str(brain(sentiment)), ''
    if err == '0' or err == '1' : 
        res, err = err, res
    if res=='1':
        return render_template('Sentimental analysis.html', result = 'https://i.pinimg.com/originals/6c/aa/38/6caa38a6954ef94b5d2f72da66f94335.png', err = err)
    if res=='0':
        return render_template('Sentimental analysis.html', result = 'https://images-na.ssl-images-amazon.com/images/I/711NDQNFqxL.png', err = err)
if __name__=="__main__":
    app.run(debug = True)

