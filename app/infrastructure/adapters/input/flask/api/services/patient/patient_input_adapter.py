from app.infrastructure.adapters.output.randomforest.patient_classification_random_forest_adapter import PatientClassificationRandomForestAdapter
from app.infrastructure.adapters.input.flask.api.services.patient import blueprint
from flask import jsonify

patient_classification_random_forest_adapter = PatientClassificationRandomForestAdapter()


@blueprint.route('/classify', methods=['GET'])
def classify():
    return jsonify(patient_classification_random_forest_adapter.classify_patient(
        90, 90, 90, 90, True, True, True, True, True, True, True, True, True, True, True, True
    ))
