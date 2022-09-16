from app.application.ports.output.patient_classification_output_port import PatientClassificationOutputPort


class PatientClassificationRandomForestAdapter(PatientClassificationOutputPort):
    def classify_patient(self, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
                         sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea):

        return {'status_code': 200, 'message': 'Classified'}

    @staticmethod
    def read(): pass

    @staticmethod
    def train(): pass

    @staticmethod
    def save(): pass
