from src.modules.agenda.aplication.ports.repository.CalendarRepositoryPort import CalendarRepositoryPort


class DeleteCalendarUseCase:
    def __init__(self, repository: CalendarRepositoryPort):
        self._repository = repository
    
    async def execute(self, ano:str) -> bool:
        try:
            await self._repository.delete(ano) 
            await self.bus.publish()
            return True
        except Exception as e:
            raise Exception("error ao criar ", e)