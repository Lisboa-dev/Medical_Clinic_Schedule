
from src.modules.agenda.domain.rules import GenericRule


class CreateGenericRuleRoomUseCase:
    def __init__(self, repository:RuleRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, command: CreateGenericRuleRoomInput):
       try:
            rule = GenericRule(command.ruleEffect, command.idToManager, command.rangeTime, command.description)
            
            if rule is None:
                return CreateRuleExeption()
            
            await self._repository.save(rule)
            await self._bus.emit()
            return rule
        
       except Exception as e:
        raise ("Exception in creating rule: ", e)