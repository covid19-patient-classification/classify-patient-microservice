from datetime import datetime


class Patient:
    def __init__(self, identification, name, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
                 sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea, covid19_severity):

        self.identification = identification
        self.name = name
        self.sato2 = sato2
        self.pao2 = pao2
        self.fio2 = fio2
        self.pf_ratio = pf_ratio
        self.respiratory_failure = respiratory_failure
        self.ards = ards
        self.sepsis_shock = sepsis_shock
        self.sore_throat = sore_throat
        self.fever = fever
        self.cough = cough
        self.headache = headache
        self.fatigue = fatigue
        self.dyspnea = dyspnea
        self.nausea = nausea
        self.vomit = vomit
        self.diarrhea = diarrhea
        self.covid19_severity = covid19_severity
        self.set_registration_date = self.set_registration_date()

    def __str__(self):
        return str(self.__dict__)

    @staticmethod
    def set_registration_date():
        return datetime.today().strftime('%Y-%m-%d %H:%M:%S')
