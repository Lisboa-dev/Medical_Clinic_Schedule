


from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import DoctorRepositoryPort


class DeleteDoctorUseCase:
    
    def __init__(self, repository:DoctorRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, doctor_id: str) -> bool:
        doctor = await self._repository.getDoctor(doctor_id)
        if doctor:
            self._bus.emit()
            return True
        return False