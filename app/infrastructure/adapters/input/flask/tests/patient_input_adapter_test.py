from app.infrastructure.adapters.input.flask.tests import BaseTestClass


class PatientInputAdapterTest(BaseTestClass):
    def test_classify_patient(self):
        patient_data = {
            "identification": "1101020304", "name": "Andrés Manuel Ponce Perez", "sato2": 89.2, "pao2": 77.2,
            "fio2": 32, "pf_ratio": 241.3, "respiratory_failure": False, "ards": False, "sepsis_shock": False,
            "fever": False, "cough": True, "sore_throat": False, "headache": False, "fatigue": False,
            "dyspnea": True, "nausea": True, "vomit": False, "diarrhea": False
        }
        headers_payload = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        response = self.client.post('api/v1/patients/', json=patient_data, headers=headers_payload)
        self.assertEqual(500, response.status_code)
