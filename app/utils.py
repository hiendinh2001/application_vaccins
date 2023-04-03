import json, os
from app import app

def read_json(path): 
    with open(path, "r") as f:
        return json.load(f)

def load_patient(name=None, gender=None):
    patients = read_json(os.path.join(app.root_path, 'data/patient.json'))

    if name:
        patients = [p for p in patients if p['name'].lower().find(name.lower()) >= 0]

    if gender:
        patients = [p for p in patients if p['gender'].lower().find(gender.lower()) >= 0]
    return patients

def load_immunization():
    immunizations = read_json(os.path.join(app.root_path, 'data/immunization.json'))

    return immunizations

def load_observation():
    observations = read_json(os.path.join(app.root_path, 'data/observation.json'))

    return observations

def load_practitioner():
    practitioners = read_json(os.path.join(app.root_path, 'data/practitioner.json'))

    return practitioners

def get_patient_by_id(patient_id):
    patients = read_json(os.path.join(app.root_path, 'data/patient.json'))

    for p in patients:
        if p['identifier'] == patient_id:
            return p

def get_immunization_by_id(immunization_id): 
    immunizations = read_json(os.path.join(app.root_path, 'data/immunization.json'))

    for i in immunizations:
        if i['identifier'] == immunization_id:
            return i

def get_observation_by_id(observation_id): 
    observations = read_json(os.path.join(app.root_path, 'data/observation.json'))

    for o in observations:
        if o['identifier'] == observation_id:
            return o

def get_practitioner_by_id(practionner_id):
    practitioners = read_json(os.path.join(app.root_path, 'data/practitioner.json'))

    for pr in practitioners:
        if pr['identifier'] == practionner_id:
            return pr