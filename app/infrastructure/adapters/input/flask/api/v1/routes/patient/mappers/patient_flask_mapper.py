from app.application.ports.input.patient_management_input_port import PatientManagementInputPort


class PatientFlaskMapper:
    @staticmethod
    def request_to_domain(request):
        data = request.json
        return PatientManagementInputPort().create_patient(
            data['identification'], data['name'], data['sato2'], data['pao2'], data['fio2'], data['pf_ratio'],
            data['respiratory_failure'], data['ards'], data['sepsis_shock'], data['sore_throat'], data['fever'],
            data['cough'], data['headache'], data['fatigue'], data['dyspnea'], data['nausea'], data['vomit'],
            data['diarrhea']
        )
