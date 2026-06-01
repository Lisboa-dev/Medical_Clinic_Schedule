

from src.modules.agenda.aplication.dtos.useCase.command.AppointmentUseCasesDTO import DeleteAppointmentCommand
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import AppointmentRepositoryPort


class DeleteAppointmentUseCase:
    def __init__(self, repository: AppointmentRepositoryPort, bus: BusPort):
        self._repository = repository
        self.bus = bus
        
    async def execute(self, command: DeleteAppointmentCommand):
        try:
            await self._repository.delete(command.id)
            await self.bus.publish()
            return True
        except Exception as e:
            raise Exception("error ao criar ", command)