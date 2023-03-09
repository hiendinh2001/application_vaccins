from flask import render_template, request, jsonify
from app import app
import utils
from utils import read_json

@app.route("/fhir")
def home(): 

    return render_template('index.html')

@app.route("/fhir/Patient")
def patient_list():
    name = request.args.get("name")
    gender = request.args.get("gender")

    patients = utils.load_patient(name=name,
                                  gender=gender)

    return render_template('patient.html', patients=patients) 

@app.route("/fhir/Patient/<int:patient_id>") 
def patient_detail(patient_id):
    patient = utils.get_patient_by_id(patient_id)

    return render_template('patient_detail.html',
                           patient=patient)

@app.route("/fhir/Immunization/<int:immunization_id>") 
def immunization_detail(immunization_id):
    immunization = utils.get_immunization_by_id(immunization_id)

    return render_template('immunization_detail.html',
                           immunization=immunization)

@app.route("/fhir/Observation/<int:observation_id>") 
def observation_detail(observation_id):
    observation = utils.get_observation_by_id(observation_id)

    return render_template('observation_detail.html',
                           observation=observation)
@app.route('/fhir/_history')
def history():
    patients = utils.load_patient()
    immunizations = utils.load_immunization()
    observations = utils.load_observation()

    return render_template('history.html',
                           patients=patients,
                           immunizations=immunizations,
                           observations=observations)

if __name__ == '__main__':
    app.run(debug=True)