from abc import ABC, abstractmethod


class PatientManagementOutputPort(ABC):
    @abstractmethod
    def persist_patient(self, patient): pass
