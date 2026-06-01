
from src.modules.agenda.aplication.dtos.useCase.command.DoctorUseCasesDTO import CreateDoctorCommand
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import DoctorRepositoryPort
from src.modules.agenda.domain.entities import Doctor



class CreateDoctorUseCase:
    
    def __init__(self, repository:DoctorRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, data:CreateDoctorCommand):
      try:
        basicRules = await self._repository.GetDoctorGenericRules()
        doctor = Doctor(data.name, data.id_extern, basicRules)
        
        if isinstance(doctor, Doctor):
            await self._repository.save(doctor)
            await self._bus.emit()
            return True
        
      except Exception as e:
        raise Exception("error ao criar ", e)