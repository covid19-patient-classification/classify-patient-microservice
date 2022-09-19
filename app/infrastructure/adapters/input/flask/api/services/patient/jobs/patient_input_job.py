from app.infrastructure.adapters.input.flask.api import celery
from app.infrastructure.adapters.output.random_forest.patient_classification_random_forest_adapter import PatientClassificationRandomForestAdapter


@celery.task
def train_async_model(patient_dataframe, covid19_severity_prediction):
    PatientClassificationRandomForestAdapter().train(patient_dataframe, covid19_severity_prediction)
