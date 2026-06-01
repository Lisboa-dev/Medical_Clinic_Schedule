from src.modules.agenda.domain.rules.BaseRule import BaseRule
from src.modules.agenda.domain.valueObjects.RangeTime import RangeTime
from ..valueObjects.Id import ID
from ..services.VerifyInRange import VerifyInRange



class Doctor:
   
    
    #id_extern: str,
    def __init__(self, name: str, rules: list[BaseRule], id: str  , availability: bool = True):
        self._id = ID(id)
        self._name = name
        self._rules = rules
        self._availability = availability
        
        
        
        
    def verifyInDisponibility(self, time: RangeTime) -> bool:
        
        if not self._availability:
            return False
        
        return VerifyInRange.execute(time, self.rules)

        
    def update():
        pass
    
    def delete():
        pass    
        
    def updateAvailability(self, time: RangeTime):
     pass
        

        
        
    def addRule(self, rule: BaseRule):
        self.rules.append(rule )
        
        
    def updateRules(self, rules: list[BaseRule]):
        self.rules = rules
        
    def deleteRule(self, rule: BaseRule):
        self.rules.remove(rule)
        
    
    def addClinicRule(self, rule: BaseRule):
        self.rules.append(rule )
        
        
    def updateClinicRules(self, rules: list[BaseRule]):
        self.rules = rules
        
    def deleteClinicRule(self, rule: BaseRule):
        self.rules.remove(rule)
        
    
    def deleteClinicRules():
        pass
    
    