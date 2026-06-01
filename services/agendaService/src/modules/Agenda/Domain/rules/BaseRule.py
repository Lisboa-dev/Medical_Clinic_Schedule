
from abc import ABC, abstractmethod
from src.modules.agenda.domain.rules.RuleEnum import RuleEffect, TargetType
from src.modules.agenda.domain.valueObjects.Id import ID
from src.modules.agenda.domain.valueObjects.Date import Date
from src.modules.agenda.domain.valueObjects.RangeTime import RangeTime


  
    
class BaseRule(ABC):
    def __init__(
        self,
        ruleEffect: RuleEffect,
        rangeTime: RangeTime = None,
        id: str = None,
        description: str = None,
        date: Date = None,
        weekday: int = None,
        target: str = None,
        targetType: TargetType = None,
        nome: str = None

      ):
        
        
        self._id= ID()if id==None else id
        self._rangeTime = rangeTime
        self._description = description
        self._date = date
        self._weekday = weekday
        self._ruleEffect = ruleEffect
        self._target = target
        self._targetType = targetType
        self._nome = nome
    
    

    def compare(self, time:RangeTime) -> bool:
        return self._rangeTime.compare(time)
    
    @property
    def rangeTime(self) -> RangeTime:
        return self._rangeTime
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def date(self) -> Date:
        return self._date
    
    @property
    def weekday(self) -> int:
        return self._weekday
    
    @property
    def ruleEffect(self) -> RuleEffect:
        return self._ruleEffect
    
    @property
    def ruleEffectPriority(self) -> RuleEffect:
        return self._ruleEffect.priority
    
    @property
    def startTime(self) -> str:
        return self._rangeTime.start_time
    
    @property
    def endTime(self) -> str:
        return self._rangeTime.end_time
    
    @property
    def target(self) -> str:
        return self._target