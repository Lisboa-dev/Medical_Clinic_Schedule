class DeleteRuleEvent:
    def __init__(self, id: str):
        self.id = id
        
        
class CreateBlockRuleEvent:
    def __init__(self, doctor: str, day: str, time: str):
        self.doctor = doctor
        self.day = day
        self.time = time
        
        
class CreateRuleEvent:
    def __init__(self, ruleEffect: str, idToManager: str, rangeTime: str, description: str):
        self.ruleEffect = ruleEffect
        self.idToManager = idToManager
        self.rangeTime = rangeTime
        self.description = description