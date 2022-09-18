from datetime import datetime


class Patient:
    def __init__(self, identification, name, sato2, pao2, fio2, pf_ratio, respiratory_failure, ards, sepsis_shock,
                 sore_throat, fever, cough, headache, fatigue, dyspnea, nausea, vomit, diarrhea):
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
        self.covid19_severity = None
        self.registration_date = self.__set_registration_date()

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return [{
            'sato2': self.sato2,
            'pao2': self.pao2,
            'fio2': self.fio2,
            'pf_ratio': self.pf_ratio,
            'respiratory_failure': self.__boolean_to_integer(self.respiratory_failure),
            'ards': self.__boolean_to_integer(self.ards),
            'sepsis_shock': self.__boolean_to_integer(self.sepsis_shock),
            'fever': self.__boolean_to_integer(self.fever),
            'cough': self.__boolean_to_integer(self.cough),
            'sore_throat': self.__boolean_to_integer(self.sore_throat),
            'headache': self.__boolean_to_integer(self.headache),
            'fatigue': self.__boolean_to_integer(self.fatigue),
            'dyspnea': self.__boolean_to_integer(self.dyspnea),
            'nausea': self.__boolean_to_integer(self.nausea),
            'vomit': self.__boolean_to_integer(self.vomit),
            'diarrhea': self.__boolean_to_integer(self.diarrhea)
        }]

    def __rules__(self):
        return {
            'case_severity': self.covid19_severity,
            'sato2': self.sato2,
            'pf_ratio': self.pf_ratio,
            'respiratory_failure': self.respiratory_failure,
            'ards': self.ards,
            'sepsis_shock': self.sepsis_shock
        }

    def set_covid19_severity(self, covid19_severity):
        self.covid19_severity = covid19_severity

    @staticmethod
    def __set_registration_date():
        return datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def __boolean_to_integer(boolean_value):
        return 1 if boolean_value else 0
