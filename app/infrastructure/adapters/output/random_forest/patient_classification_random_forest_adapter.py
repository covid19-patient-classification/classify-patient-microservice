from app.application.ports.output.patient_classification_output_port import PatientClassificationOutputPort
from app.infrastructure.adapters.output.random_forest.mappers.patient_random_forest_mapper import PatientRandomForestMapper
import joblib


class PatientClassificationRandomForestAdapter(PatientClassificationOutputPort):
    def __init__(self):
        self.model_path = 'app/infrastructure/adapters/output/random_forest/resources/model.joblib'
        self.random_forest_model = self.__set_up_model()

    def classify_patient(self, patient):
        patient_dataframe = PatientRandomForestMapper.patient_domain_to_dataframe(patient)
        covid19_severity_prediction = self.__predict(patient_dataframe)
        return PatientRandomForestMapper.covid19_severity_prediction_to_string(covid19_severity_prediction[0])

    def __set_up_model(self):
        return joblib.load('{}'.format(self.model_path))

    def __predict(self, patient_dataframe):
        return self.random_forest_model.predict(patient_dataframe)

    def __train(self): pass

    def __save(self):
        joblib.dump(self.random_forest_model, self.model_path)
