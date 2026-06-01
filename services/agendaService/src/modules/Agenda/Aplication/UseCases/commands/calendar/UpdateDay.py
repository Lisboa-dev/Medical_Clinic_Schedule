from src.modules.agenda.domain.entities import Day


class UpsateDayUseCase:
    def __init__(self, repository: CalendarRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, command: UpdateDayCommand):
        try:
            data = await self._repository.get(command.id)
            day = Day(data)
            dayUpdated = day.update(command.data)
            await self._repository.updateDay(dayUpdated)
            await self._bus.publish()
            return True
        except Exception as e:
            raise Exception("error ao criar ", command)