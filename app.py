# import dependencies
# from models import create_classes
import os
# import numpy as np
# import pickle #Initialize the flask App
# from flask import Flask, render_template, jsonify, request, redirect
# from sklearn import preprocessing
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn import metrics
# from sklearn.metrics import confusion_matrix
# import statsmodels.api as sm
# from sklearn import linear_model

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# model = pickle.load(open('model.pkl', 'rb'))

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# Loan = create_classes(db)

# create route that renders index.html template
@app.route("/")

def home():
    return render_template("index.html")


# Render prediction
# @app.route("/predict", methods=["GET", "POST"])

# def predict():
#     #For rendering results on HTML GUI
#     int_features = [float(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
#     output = round(prediction[0], 2) 

#     return render_template('index.html', prediction_text='Liklihood of loan default is :{}'.format(output))


#Render results
# @app.route('/results',methods=['POST'])

# def results():

#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
