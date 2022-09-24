from abc import ABC, abstractmethod


# Interface
class PatientClassificationOutputPort(ABC):
    @abstractmethod
    def classify_patient(self, patient): pass
    