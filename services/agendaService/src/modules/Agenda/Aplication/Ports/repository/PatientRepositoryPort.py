
from abc import ABC, abstractmethod

class PatientRepositoryPort(ABC):
    @abstractmethod
    def save(self, patient:Patient) -> None:
        pass
    
    @abstractmethod
    def update(self, patient:Patient) ->None:
        pass
    
    def delete(self, patient_id:str) -> None:
        pass