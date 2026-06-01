from abc import ABC, abstractmethod

class RuleRepositoryPoty(ABC):
    
    @abstractmethod
    def save(self, rule:Rule) -> None:
        pass
    
    @abstractmethod
    def delete(self, id:str) -> None:
        pass