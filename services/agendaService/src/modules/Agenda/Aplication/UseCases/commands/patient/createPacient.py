

from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import PatientRepositoryPort

from services.usersService.src.Infra.Mapper.domain import Pacient


class CreatePacientUseCase:
    def __init__(self, repository: PatientRepositoryPort, bus: BusPort):
        self.repository = repository
        self._bus = bus
    
    async def execute(self, command: CreatePacientCommand) -> bool:
       
       try:
            pacient = Pacient(**command.data)
            
            await self.repository.save(pacient)
            await self._bus.emit()
            
            return True 
            
       except Exception as e:
            return