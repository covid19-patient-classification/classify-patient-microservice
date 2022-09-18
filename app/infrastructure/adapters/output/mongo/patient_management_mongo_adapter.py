from app.application.ports.output.patient_management_output_port import PatientManagementOutputPort


class PatientManagementMongoAdapter(PatientManagementOutputPort):
    def persist_patient(self, patient): pass
