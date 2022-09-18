from app.infrastructure.adapters.input.flask.api.services.patient import blueprint
from app.infrastructure.adapters.input.flask.api.services.patient.mappers.patient_flask_mapper import PatientFlaskMapper
from app.infrastructure.adapters.output.random_forest.patient_classification_random_forest_adapter import PatientClassificationRandomForestAdapter
from app.infrastructure.adapters.output.mongodb.patient_management_mongodb_adapter import PatientManagementMongoDBAdapter
from flask import abort, jsonify, request


@blueprint.route('/', methods=['POST'])
def classify():
    try:
        patient = PatientFlaskMapper().request_to_domain(request)
        covid19_severity = PatientClassificationRandomForestAdapter().classify_patient(patient)
        patient.set_covid19_severity(covid19_severity)
        return jsonify(PatientManagementMongoDBAdapter().persist_patient(patient))
    except Exception as e:
        return abort(500, e)
