from abc import ABC, abstractmethod


class PatientManagementUseCase(ABC):
    @abstractmethod
    def create_patient(
            self, identification, name, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
            sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea, covid19_severity
    ): pass

    @abstractmethod
    def retrieve_patient(self, identification): pass
