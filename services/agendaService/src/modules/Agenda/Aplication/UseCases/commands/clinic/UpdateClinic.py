
from src.modules.agenda.aplication.dtos.useCase.command.ClinicUseCasesDTO import UpdateClinicCommand
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import ClinicRepositoryPort


class UpdateClinicUseCase:
    
    def __init__(self, repository: ClinicRepositoryPort, bus: BusPort):
        self._repository =repository 
        self.bus = bus
        
    def execute(self, data:UpdateClinicCommand): 
        try:
            clinic = self._repository.getClinic()
            clinic.update(data)
            self._repository.update(clinic)
            self.bus.emit()
        except Exception as e:
            raise Exception("error ao criar ", e)