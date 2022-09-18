from abc import ABC, abstractmethod


# Interface
class PatientClassificationUseCase(ABC):
    @abstractmethod
    def classify_patient(self, patient): pass
