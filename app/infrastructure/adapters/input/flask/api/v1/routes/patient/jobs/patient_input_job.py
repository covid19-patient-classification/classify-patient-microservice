from app.infrastructure.adapters.output.mongodb.patient_management_mongodb_adapter import PatientManagementMongoDBAdapter
from multiprocessing import Process


def persist_async_patient(patient):
    persist_process = Process(
        target=PatientManagementMongoDBAdapter().persist_patient,
        args=(patient,)
    )
    persist_process.start()
