from app.infrastructure.adapters.input.flask.api.v1.routes.patient import blueprint
from app.infrastructure.adapters.input.flask.api.v1.routes.patient.jobs import patient_input_job
from app.infrastructure.adapters.input.flask.api.v1.routes.patient.mappers.patient_flask_mapper import PatientFlaskMapper
from app.infrastructure.adapters.output.random_forest.patient_classification_random_forest_adapter import PatientClassificationRandomForestAdapter
from flask import abort, jsonify, request


@blueprint.route('/', methods=['POST'])
def classify():
    try:
        patient = PatientFlaskMapper().request_to_domain(request)
        decision_rules = PatientClassificationRandomForestAdapter().classify_patient(patient)
        patient_input_job.persist_async_patient(patient)  # Background task
        return jsonify(decision_rules), 200
    except Exception as e:
        abort(500, e)
