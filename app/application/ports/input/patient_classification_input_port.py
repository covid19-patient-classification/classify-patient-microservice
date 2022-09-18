from app.application.usecases.patient_classification_use_case import PatientClassificationUseCase
from app.application.ports.output.patient_classification_output_port import PatientClassificationOutputPort


# Implement PatientClassificationUseCase Interface
class PatientClassificationInputPort(PatientClassificationUseCase):
    def classify_patient(self, patient):
        return PatientClassificationOutputPort().classify_patient(patient)
