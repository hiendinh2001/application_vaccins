import json, os
from app import app

def read_json(path): 
    with open(path, "r") as f:
        return json.load(f)

def load_patient(name=None, gender=None, from_date=None, to_date=None):
    patients = read_json(os.path.join(app.root_path, 'data/patient.json'))

    if name:
        patients = [p for p in patients if p['name'].lower().find(name.lower()) >= 0]

    if gender:
        patients = [p for p in patients if p['gender'].lower().find(gender.lower()) >= 0]
    return patients

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

def get_last_updated_date(directory=None, file_type=None):
    dates = []

    if directory is None:
        directory = os.path.join(app.root_path, 'data')

    for root, dirs, files in os.walk(directory):
        for name in files:
            if file_type is None or name.startswith(file_type):
                path = os.path.join(root, name)
                date = os.path.getmtime(path)
                dates.append((date, path))

    dates.sort(reverse=True)

    return [date for date, path in dates]


def filter_last_updated_date(dates, last_updated):
    if last_updated:
        filtered_dates = []
        for date in dates:
            if date.startswith(last_updated):
                filtered_dates.append(date)
        dates = filtered_dates
    return dates


def load_history(file_type=None, last_updated=None):
    dates = get_last_updated_date(file_type=file_type)
    dates = filter_last_updated_date(dates, last_updated)
    return dates
