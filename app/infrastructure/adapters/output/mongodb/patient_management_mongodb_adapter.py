from app.application.ports.output.patient_management_output_port import PatientManagementOutputPort
from app.infrastructure.adapters.output.mongodb.mappers.patient_management_mongodb_mapper import PatientManagementMongoDBMapper
from pymongo import MongoClient
import os


class PatientManagementMongoDBAdapter(PatientManagementOutputPort):
    def __init__(self):
        self.database = self.__setup_mongo_database()

    def persist_patient(self, patient):
        patient_data = PatientManagementMongoDBMapper().patient_domain_to_data(patient)
        self.database['patients'].insert_one(patient_data)

    @staticmethod
    def __setup_mongo_database():
        client = MongoClient(os.environ.get('DATABASE_DEPLOYMENT_URL'), connect=False)
        return client.get_database(os.environ.get('DATABASE_NAME'))
