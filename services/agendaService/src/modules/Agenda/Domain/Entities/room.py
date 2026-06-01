from src.modules.agenda.domain.entities.Appointment import Appointment
from src.modules.agenda.domain.rules.BaseRule import BaseRule
from src.modules.agenda.domain.services import VerifyInRange
from src.modules.agenda.domain.valueObjects.Id import ID
from src.modules.agenda.domain.valueObjects.RangeTime import RangeTime



class Room:
    id: ID
    name: str
    availability: bool
    status: str
    rules: list[BaseRule]
    appointmentList: list[Appointment]
  
    
    def __init__(self, name: str,rules: list[BaseRule], disponibility: bool = True, id:str = None):
        self.name = name
        self.disponibility = disponibility
        self.rules = rules
        self.id = ID.generate_id()  if id==None else ID(id)
        
    def verifyDisponibility(self, time: RangeTime) -> bool:
        if self.availability:
            return False
        
         
        if VerifyInRange.execute(time, self.rules):
            for appointment in self.appointmentList:
                if appointment.verifyOverleaps(time):
                    return False
        else:
            return False
        
        return True
    
   
       

        
    @property
    def disponibility(self):
        return self.__disponibility
    
    @property
    def disponibility(self):
        return self.__disponibility

 