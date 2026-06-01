




from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import PatientRepositoryPort
from src.modules.agenda.domain.entities.Patient import Patient


class DeletePatientUseCase:
    def __init__(self, repository: PatientRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, id: str):
        try:
            
            pacient = await self._repository.getPacient(id)
            if not isinstance(pacient, Patient):
              raise Exception("Paciente não encontrado")
            
            if pacient.destroy():
                await self._repository.delete(id)
                return True 
            
            self._bus.emit()
            
        except Exception as e:
            return False