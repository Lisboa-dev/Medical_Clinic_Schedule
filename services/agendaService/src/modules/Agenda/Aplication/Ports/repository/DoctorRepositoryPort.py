
from abc import ABC, abstractmethod


class DoctorRepositoryPort(ABC):
    @abstractmethod
    def save(self, doctor:Doctor) -> None:
        pass
    
    @abstractmethod
    def update(self, doctor:Doctor) -> None:
        pass
    
    @abstractmethod
    def delete(self, doctor_id:str) -> None:
        pass