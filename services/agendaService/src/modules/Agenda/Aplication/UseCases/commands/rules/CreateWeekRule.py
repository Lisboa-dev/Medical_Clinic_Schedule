from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.dtos.command.RulesRoomUseCasesDTO import CreateSpecificDayRoomInput
from src.modules.agenda.domain.rules.WeekRule import WeekRuleRoom


class CreateSpecificRuleRoomUseCase:
    def __init__(self, repository: RuleRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, command: CreateWeekRuleRoomInput):
        try:
            rule = WeekRuleRoom(command.ruleEffect, command.idToManager, command.rangeTime, command.description, command.weekDay)
            if rule is Exception:
                return rule
            
            await self._repository.save(rule)
            await self._bus.emit()
            return rule
            
        except Exception as e:
            raise ("Exception in creating rule: ", e)