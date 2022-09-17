from app.domain.entity.patient import Patient
from app.infrastructure.adapters.output.random_forest.patient_classification_random_forest_adapter import PatientClassificationRandomForestAdapter
from app.infrastructure.adapters.input.flask.api.services.patient import blueprint
from flask import jsonify


@blueprint.route('/classify', methods=['GET'])
def classify():
    patient = Patient("1100000000", "CXXXXXX", 95, 90, 90, 290, True,
                      True, True, True, True, True, True, True, True, True, True, True)
    covid19_severity = PatientClassificationRandomForestAdapter().classify_patient(patient)
    patient.set_covid19_severity(covid19_severity) # Aquí se puede agregar una nueva funcionalidad en el caso de uso de management
    return jsonify(patient.__rules__())
