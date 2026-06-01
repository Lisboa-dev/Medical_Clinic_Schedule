from abc import ABC, abstractmethod
class ClinicRepositoryPort(ABC):
    
    @abstractmethod
    def save(self, clinic) -> None:
        pass
    
    def update(self, clinic) -> None:
        pass 
    
    def delete(self, id:str) -> None:
        pass