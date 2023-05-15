# import necessary libraries
import os
import pandas as pd
import pickle
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    
)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
# 'or' allows us to later switch from 'sqlite' to an external database like 'postgres' easily
# os.environ is used to access 'environment variables' from the operating system
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# TODO: Add data models if needed

with app.app_context():
    db.create_all()

#################################################
# Model Setup
#################################################

# from joblib import load
# model_path = os.environ.get('MODEL_PATH', '') or "Group4_model.h5"
# print("Loading model...")
# model = load(model_path)

# from keras.models import load_model
model_path = os.path.join("finalized_model.sav")
# model = load_model(model_path)
model = pickle.load(open(model_path,'rb'))

#################################################
# Web User Interface - Front End
#################################################
# note that UI routes return a html response
# you can add as many html pages as you need
# below is an example to get you started...

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")




#################################################
# API - Back End
#################################################
# we will use '/api/..' for our api within flask application
# note that api returns a JSON response
# you can add as many API routes as you need
# below is an example to get you started...

@app.route("/risk", methods=["POST"])
def predict():
    labels = ['Less risk','High risk']
    print(request.form)
 
    index = int(model.predict(
        [
            [
            int(request.form["HighBP"]),
            int(request.form["HighChol"]),
            int(request.form["CholCheck"]),
            int(request.form["BMI"]),
            int(request.form["Smoker"]),
            int(request.form["Stroke"]),
            int(request.form["HeartDiseaseorAttack"]),
            int(request.form["PhysActivity"]),
            int(request.form["Fruits"]),
            int(request.form["Veggies"]),
            int(request.form["HvyAlcoholConsump"]),
            int(request.form["AnyHealthcare"]),
            int(request.form["NoDocbcCost"]),
            int(request.form["GenHlth"]),
            int(request.form["MentHlth"]),
            int(request.form["PhysHlth"]),
            int(request.form["DiffWalk"]),
            int(request.form["Sex"]),
            int(request.form["Age"]),
            int(request.form["Education"]),
            int(request.form["Income"]),
            ],
        ]
    )[0])
    return render_template("result.html", result_r=labels[index])

# jsonify(f"Predicted risk of getting Diabetes {labels[index]}")


if __name__ == "__main__":

    # run the flask app
    app.run()
