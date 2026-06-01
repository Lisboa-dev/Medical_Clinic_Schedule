from src.modules.agenda.aplication.dtos.useCase.command.AppointmentUseCasesDTO import UpdateAppointmentCommand
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import AppointmentRepositoryPort
from src.modules.agenda.domain.entities import Appointment


class UpdateAppointment:
    def __init__(self, repository: AppointmentRepositoryPort, bus: BusPort):
        self._repository = repository
        self.bus = bus
        
    async def execute(self, command:UpdateAppointmentCommand):
        
       try:
           appointment = await self._repository.getAppointment(id=command.id)
        
           if isinstance(appointment, Appointment):
                appointment.update(command.data)
                await self._repository.save(appointment)
                await self.bus.publish()
                return True
    
       except Exception as e:
            raise Exception("error ao criar ", command)
        