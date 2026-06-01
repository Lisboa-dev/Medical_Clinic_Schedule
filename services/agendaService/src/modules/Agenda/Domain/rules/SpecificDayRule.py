
from src.modules.agenda.domain.rules import Target
from src.modules.agenda.domain.valueObjects.RangeTime import RangeTime
from src.modules.agenda.domain.rules.RuleEnum import RuleEffect
from src.modules.agenda.domain.rules.BaseRule import BaseRule
from src.modules.agenda.domain.valueObjects.Date import Date


class SpecificDayRule(BaseRule):
    
    def __init__(
        self,
        ruleEffect: RuleEffect,
        rangeTime: RangeTime,
        description: str,
        date: Date,
        target: str = None,
        targetType: Target = None,
        nome:str = None
    ):
        super().__init__(
            ruleEffect=ruleEffect,
            rangeTime=rangeTime,
            description=description,
            date=date,
            target=target,
            targetType=targetType,
            nome=nome
        )