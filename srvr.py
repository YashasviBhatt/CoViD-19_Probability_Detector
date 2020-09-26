# Importing libraries

import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# loading trained model
with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)

@app.route('/', methods=["GET", "POST"])
def calc_prob():
    if request.method == "POST":
        filledDetails = request.form
        age = int(filledDetails['age'])
        fever = int(filledDetails['fever'])
        runnyNose = int(filledDetails['runnyNose'])
        diffBreath = int(filledDetails['diffBreath'])
        pain = int(filledDetails['pain'])

        input_features = [fever, pain, age, runnyNose, diffBreath]
        infProb = clf.predict_proba([input_features])[0][1]
        return render_template("result.html", inf=round(infProb * 100))
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)