from app.application.usecases.patient_management_use_case import PatientManagementUseCase
from app.application.ports.output.patient_management_output_port import PatientManagementOutputPort
from app.domain.entity.patient import Patient


class PatientManagementInputPort(PatientManagementUseCase):
    def __init__(self):
        self.patient_management_output_port = PatientManagementOutputPort()

    def create_patient(self, identification, name, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
                       sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea, covid19_severity):
        patient = Patient(
            identification, name, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
            sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea, covid19_severity
        )
        return patient

    def persist_patient(self, patient):
        return self.patient_management_output_port.persist_patient(patient)
