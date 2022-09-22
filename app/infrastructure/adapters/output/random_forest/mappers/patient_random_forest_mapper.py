import pandas as pd
import json


class PatientRandomForestMapper:
    @staticmethod
    def patient_domain_to_dataframe(patient):
        return pd.DataFrame.from_dict(patient.__repr__())

    @staticmethod
    def covid19_severity_prediction_to_string(covid19_severity_prediction):
        with open('app/infrastructure/adapters/output/random_forest/resources/classes.json') as classes_file:
            type_of_patients = json.load(classes_file)
            return type_of_patients[str(covid19_severity_prediction)]
