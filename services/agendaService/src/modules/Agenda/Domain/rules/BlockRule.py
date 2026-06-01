from src.modules.agenda.domain.valueObjects.Date import Date
from src.modules.agenda.domain.rules.RuleEnum import RuleEffect
from src.modules.agenda.domain.rules.BaseRule import BaseRule


class BlockRule(BaseRule):
    
    def __init__(
        self,
        date: Date = None,
        weekday: int = None,
        description: str = None,
        target: str = None,
        targetType: str = None,
        nome:str = None
    ):
        
        super().__init__(
            ruleEffect=RuleEffect.BLOCKED,
            date=date,
            weekday=weekday,
            description=description,
            target=target,
            targetType=targetType,
            nome=nome
        )
           
        
    