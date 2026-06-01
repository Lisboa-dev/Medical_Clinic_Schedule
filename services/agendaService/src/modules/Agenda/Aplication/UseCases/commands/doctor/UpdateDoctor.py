



from src.modules.agenda.aplication.dtos.useCase.command.DoctorUseCasesDTO import UpdateDoctorCommand
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import DoctorRepositoryPort


class CreateDoctorUseCase:
    
    def __init__(self, repository:DoctorRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, data:UpdateDoctorCommand):
        
        doctor = await self._repository.get(data)
        
        if doctor:
            await self._bus.emit()
            return True
        
        return None