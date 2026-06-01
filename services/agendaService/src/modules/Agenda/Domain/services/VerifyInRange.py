from src.modules.agenda.domain.rules.BaseRule import BaseRule



from enum import IntEnum

from src.modules.agenda.domain.rules.RuleEnum import RuleEffect



class VerifyInRange:
    
    @staticmethod
    def execute( rule: BaseRule, rules: list[BaseRule]) -> bool:
        
        rules.sort(key=lambda rule: (rule.ruleEffectPriority, rule.startTime))
        
        for r in rules:
           if r.date.compare(rule.date) or r.weekday == rule.weekday or (r.date==None and r.weekday==None):
               if r.ruleEffect == RuleEffect.BLOCK:
                   return False
               
               if r.ruleEffect == RuleEffect.ADD and r.rangeTime.overlaps(rule.rangeTime):
                   return True
               
               if r.ruleEffect == RuleEffect.REMOVE and r.rangeTime.overlaps(rule.rangeTime):
                   return False
                   
        return False