from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.domain.rules.BlockRule import BlockRuleRoom

class CreateBlockRuleRoomUseCase:
    def __init__(self, repository: RuleRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, command: CreateBlockRuleRoomCommand) -> bool:
        try:
            rule = BlockRuleRoom(ruleEffect=command.ruleEffect, date=command.date, weekday=command.weekday, description=command.description)
            
            if(isinstance(rule, BlockRuleRoom)):
                await self._repository.save(rule)
                await self._bus.emit()
                return rule
            
            return 
        except Exception as e:
            raise ("Exception in creating rule: ", e)
        