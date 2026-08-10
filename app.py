from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np


app = Flask(__name__)


with open("model/model1.pkl","rb") as f:
    
    model = pickle.load(f)
         

with open("model/model2.pkl", "rb") as f:
    
    type_model = pickle.load(f)

 
    

# ---- Routes for Pages ----
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/preven")
def preven():
    return render_template("preven.html")

@app.route("/predict_page")
def predict_page():
    return render_template("prediction.html")


@app.route("/symptoms")
def symptoms():
    return render_template("symptoms.html")

@app.route("/types")
def types():
    return render_template("types.html")



# ---- API for Prediction ----
@app.route('/predict', methods=['POST'])
def predict():
    # Extract data in correct order
    # features = [
    #     float(request.form['Pregnancies']),
    #     float(request.form['Glucose']),
    #     float(request.form['BloodPressure']),
    #     float(request.form['SkinThickness']),
    #     float(request.form['Insulin']),
    #     float(request.form['BMI']),
    #     float(request.form['DiabetesPedigreeFunction']),
    #     float(request.form['Age'])
    # ]
    
    
    # prediction = model.predict([np.array(features)])

    features = [float(x) for x in request.form.values()]
    prediction = model.predict([np.array(features)])
    return jsonify({'prediction': int(prediction[0])})
    
    

@app.route('/predict_type', methods=['POST'])
def predict_type():
    features = [
        float(request.form['Age']),
        float(request.form['Gender']),
        float(request.form['Pregnant']),
        float(request.form['BMI']),
        float(request.form['FamilyHistory']),
        float(request.form['FastingGlucose']),
        float(request.form['OGTT_0min']),
        float(request.form['OGTT_60min']),
        float(request.form['OGTT_120min']),
        float(request.form['InsulinLevel']),
        float(request.form['CPeptideLevel']),
        float(request.form['AutoimmuneMarker'])
    ]
    
    my_prediction = type_model.predict([np.array(features)])
    if(my_prediction[0] == 'Type 1'):
        my_prediction[0] = 0
    elif(my_prediction[0] == 'Type 2'):
        my_prediction[0] = 1
    else:
        my_prediction[0] = 2
    return jsonify({'type_prediction': int(my_prediction[0])})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
