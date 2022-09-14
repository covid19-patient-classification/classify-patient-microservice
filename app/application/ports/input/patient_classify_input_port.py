from app.application.usecases.patient_classify_use_case import PatientClassifyUseCase
from app.application.ports.output.patient_classify_output_port import PatientClassifyOutputPort


# Implement PatientClassifyUseCase Interface
class PatientClassifyInputPort(PatientClassifyUseCase):

    def __init__(self):
        self.patient_classify_output_port = PatientClassifyOutputPort()

    def create_patient(self, identification, name, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
                       sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea,
                       covid19_severity):

        return self.patient_classify_output_port.create_patient(
            identification, name, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
            sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea, covid19_severity
        )

    def classify_patient(self, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
                         sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea):
        return self.patient_classify_output_port.classify_patient(
            sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock, sore_throat,
            fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea
        )
