from app.application.ports.output.patient_classification_output_port import PatientClassificationOutputPort
from app.infrastructure.adapters.output.random_forest.mappers.patient_random_forest_mapper import PatientRandomForestMapper
import joblib


class PatientClassificationRandomForestAdapter(PatientClassificationOutputPort):
    def __init__(self):
        self.model_path = 'app/infrastructure/adapters/output/random_forest/resources/model.joblib'
        self.random_forest_model = self.set_up_model(self.model_path)

    def classify_patient(self, patient):
        patient_dataframe = PatientRandomForestMapper.patient_domain_to_dataframe(patient)
        covid19_severity_prediction = self.predict(self.random_forest_model, patient_dataframe)
        return PatientRandomForestMapper.covid19_severity_prediction_to_string(covid19_severity_prediction[0])

    @staticmethod
    def set_up_model(model_path):
        return joblib.load('{}'.format(model_path))

    @staticmethod
    def predict(random_forest_model, patient_dataframe):
        return random_forest_model.predict(patient_dataframe)

    @staticmethod
    def train(): pass

    @staticmethod
    def save(random_forest_model, model_path):
        joblib.dump(random_forest_model, model_path)
