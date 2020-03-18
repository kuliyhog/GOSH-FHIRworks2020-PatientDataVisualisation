from flask import Flask, render_template, url_for, jsonify
from fhir_parser import FHIR
import datetime, time

app = Flask(__name__)

@app.route('/')
def index():
    fhir = FHIR()
    patients = fhir.get_all_patients()
    return render_template('patients.html', patients=patients)
    
@app.route('/patient/<string:id>')
def patient(id):
    fhir = FHIR()
    patient = fhir.get_patient(id)
    observations = fhir.get_patient_observations(id)

    return render_template('patientinfo.html', observations=observations, patient=patient)

@app.route('/statistics/<string:id>')
def getstatistics(id):
    fhir = FHIR()
    patient = fhir.get_patient(id)
    observations = fhir.get_patient_observations(id)

    bp_dict = {
        "date": [],
        "dbp": [],
        "sbp": []
    }

    hr_dict = {
        "date": [],
        "hr": []
    }

    rr_dict = {
        "date": [],
        "rr": []
    }

    bw_dict = {
        "date": [],
        "bw": []
    }

    bh_dict = {
        "date": [],
        "bh": []
    }

    bmi_dict = {
        "date": [],
        "bmi": []
    }

    bmip_dict = {
        "date": [],
        "bmip": []
    }

    temp_bp_dates = []
    bp_observations = []
    temp_hr_dates = []
    hr_observations = []
    temp_rr_dates = []
    rr_observations = []

    temp_bw_dates = []
    bw_observations = []
    temp_bh_dates = []
    bh_observations = []
    temp_bmi_dates = []
    bmi_observations = []
    temp_bmip_dates = []
    bmip_observations = []
    
    for observation in observations:
        if observation.components[0].display == "Blood Pressure":
            bp_observations.append(observation)
            temp_bp_dates.append(observation.effective_datetime)

        if observation.components[0].display == "Heart rate":
            hr_observations.append(observation)
            temp_hr_dates.append(observation.effective_datetime)

        if observation.components[0].display == "Respiratory rate":
            rr_observations.append(observation)
            temp_rr_dates.append(observation.effective_datetime)

        if observation.components[0].display == "Body Weight":
            bw_observations.append(observation)
            temp_bw_dates.append(observation.effective_datetime)
        
        if observation.components[0].display == "Body Height":
            bh_observations.append(observation)
            temp_bh_dates.append(observation.effective_datetime)

        if observation.components[0].display == "Body Mass Index":
            bmi_observations.append(observation)
            temp_bmi_dates.append(observation.effective_datetime)

        if observation.components[0].display == "Body mass index (BMI) [Percentile] Per age and gender":
            bmip_observations.append(observation)
            temp_bmip_dates.append(observation.effective_datetime)
    
    temp_hr_dates.sort()
    temp_bp_dates.sort()
    temp_rr_dates.sort()
    temp_bw_dates.sort()
    temp_bh_dates.sort()
    temp_bmi_dates.sort()
    temp_bmip_dates.sort()

    for i in range(0, len(temp_bp_dates)):
        for observation in bp_observations:
            if temp_bp_dates[i] == observation.effective_datetime:
                bp_dict["date"].append(int(time.mktime(temp_bp_dates[i].timetuple())) * 1000)
                bp_dict["dbp"].append(observation.components[1].value)
                bp_dict["sbp"].append(observation.components[2].value)
                break

    for i in range(0, len(temp_hr_dates)):
        for observation in hr_observations:
            if temp_hr_dates[i] == observation.effective_datetime:
                hr_dict["date"].append(int(time.mktime(temp_bp_dates[i].timetuple())) * 1000)
                hr_dict["hr"].append(observation.components[0].value)
                break

    for i in range(0, len(temp_rr_dates)):
        for observation in rr_observations:
            if temp_rr_dates[i] == observation.effective_datetime:
                rr_dict["date"].append(int(time.mktime(temp_bp_dates[i].timetuple())) * 1000)
                rr_dict["rr"].append(observation.components[0].value)
                break

    for i in range(0, len(temp_bw_dates)):
        for observation in bw_observations:
            if temp_bw_dates[i] == observation.effective_datetime:
                bw_dict["date"].append(int(time.mktime(temp_bp_dates[i].timetuple())) * 1000)
                bw_dict["bw"].append(observation.components[0].value)
                break

    for i in range(0, len(temp_bh_dates)):
        for observation in bh_observations:
            if temp_bh_dates[i] == observation.effective_datetime:
                bh_dict["date"].append(int(time.mktime(temp_bp_dates[i].timetuple())) * 1000)
                bh_dict["bh"].append(observation.components[0].value)
                break

    for i in range(0, len(temp_bmi_dates)):
        for observation in bmi_observations:
            if temp_bmi_dates[i] == observation.effective_datetime:
                bmi_dict["date"].append(int(time.mktime(temp_bp_dates[i].timetuple())) * 1000)
                bmi_dict["bmi"].append(observation.components[0].value)
                break

    for i in range(0, len(temp_bmip_dates)):
        for observation in bmip_observations:
            if temp_bmip_dates[i] == observation.effective_datetime:
                bmip_dict["date"].append(int(time.mktime(temp_bp_dates[i].timetuple())) * 1000)
                bmip_dict["bmip"].append(observation.components[0].value)
                break

    return render_template('statistics.html', patient=patient, bp_dict=bp_dict, hr_dict=hr_dict, rr_dict=rr_dict, bw_dict=bw_dict, bh_dict=bh_dict, bmi_dict=bmi_dict, bmip_dict=bmip_dict)


@app.route('/averageage')
def getaverageage():
    fhir = FHIR()
    patients = fhir.get_all_patients()
    ages = []
    for patient in patients:
        ages.append(patient.age())

    return str(sum(ages)/len(ages))

@app.route('/observationstats')
def observationstats():
    fhir = FHIR()
    patients = fhir.get_all_patients()
    observations = []

    for patient in patients:
        observations.extend(fhir.get_patient_observations(patient.uuid))

    total_obsv = len(observations)

    observation_types = [observation.type for observation in observations]
    most_frequent_observation_type = max(set(observation_types), key=observation_types.count)

    observation_components = []
    for observation in observations:
        observation_components.extend(observation.components)

    total_obsv_components = len(observation_components)

    observation_component_types = [observation_component.display for observation_component in observation_components]
    most_frequent_observation_component_type = max(set(observation_types), key=observation_types.count)

    obsvstats_dictionary = {
        "totalObsv": total_obsv,
        "mfObservationType": most_frequent_observation_type,
        "totalObsvComp": total_obsv_components,
        "mfObsvCompType": most_frequent_observation_component_type
    }
    
    response = jsonify(obsvstats_dictionary)
    return response


if __name__ == "__main__":
    app.run(debug=True)