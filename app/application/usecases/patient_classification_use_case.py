from abc import ABC, abstractmethod


# Interface
class PatientClassificationUseCase(ABC):
    @abstractmethod
    def classify_patient(
            self, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
            sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea
    ): pass