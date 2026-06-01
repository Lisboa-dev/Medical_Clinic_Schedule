



from src.modules.agenda.aplication.dtos.useCase.command.ClinicUseCasesDTO import CreateClinicCommand
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import ClinicRepositoryPort
from src.modules.agenda.domain.entities import Clinic


class CreateClinicUseCase:
    
    def __init__(self, repository: ClinicRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
    
    async def execute(self, command:CreateClinicCommand):
        # Lógica para criar um administrador
        try:
         clinic = Clinic(command.data)
         await self._repository.save(clinic)
         self._bus.emit()
        except Exception as e:
            raise ("Exception in creating clinic: ", e)
        return True