class PatientManagementMongoDBMapper:
    @staticmethod
    def patient_domain_to_data(patient):
        return patient.__dict__
