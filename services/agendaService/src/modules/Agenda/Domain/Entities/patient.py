

from src.modules.agenda.domain.valueObjects.Id import ID


class Patient:
    id: ID
    name: str
    appoiments: list[str]
   


    def __init__(self, id: str, name: str):
        self.id = ID(id)
        self.name = name
        
    def add_appoiment(self, appoiment: str):
        self.appoiments.append(appoiment)
 
