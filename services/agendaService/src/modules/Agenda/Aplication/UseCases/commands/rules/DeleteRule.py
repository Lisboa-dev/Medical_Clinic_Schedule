

class DeleteRuleUseCase:
    def __init__(self, repository: RuleRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, rule_id: str) -> bool:
        
        rule = await self._repository.deleteRule(rule_id)

        if rule is Exception:
            raise rule

        
        self._bus.emit()

        return True