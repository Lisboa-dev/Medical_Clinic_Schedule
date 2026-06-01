from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.dtos.input.RulesRoomUseCasesDTO import CreateSpecificDayRoomInput
from src.modules.agenda.domain.rules.SpecificRuleRoom import SpecificRuleRoom


class CreateSpecificRuleRoomUseCase:
    def __init__(self, repository: RuleRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, command: CreateSpecificRoomInput):
      try:
          rule = SpecificRuleRoom(command.ruleEffect, command.idToManager, command.rangeTime, command.description, input.rom_id)
          if rule is None:
               return CreateRuleException()
           
          await self._repository.save(rule)
          await self._bus.emit()
          return rule
         
      except Exception as e:
          raise ("Exception in creating rule: ", e)