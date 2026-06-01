from binascii import Error

from src.modules.agenda.aplication.dtos.repositorys.input import AppointmentSchedulingInputDTO
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository.AppointmentRepositoryPort import AppointmentRepositoryPort
from src.modules.agenda.aplication.ports.repository.AppointmentSchedulingRepositoryPort import AppointmentSchedulingRepositoryPort
from src.modules.agenda.aplication.dtos.useCase.command.AppointmentUseCasesDTO import CreateAppointmentCommand
from src.modules.agenda.domain.entities import Appointment


class CreateAppoimentUseCase:
    def __init__(self, repositoryAppointment: AppointmentRepositoryPort, repositorySchedulingContext: AppointmentSchedulingRepositoryPort, bus: BusPort):
        self._repositoryAppointment = repositoryAppointment
        self._repositorySchedulingContext = repositorySchedulingContext
        self._bus = bus
        
    async def execute(self, command:CreateAppointmentCommand):
        try:
            
            
            context = await self._repositorySchedulingContext.getContext(
                AppointmentSchedulingInputDTO(
                    date=command.date, 
                    weekday=command.weekday, 
                    doctor=command.doctor, 
                    patient=command.patient, 
                    time=command.time,
                    type=command.type,
                )
            )
            
            appointment = Appointment.create(
                patient=command.patient,
                doctor=command.doctor,
                room=command.room,
                day=context.day,
                time=context.time,
                type=context.type
            )
           
            if isinstance(appointment, Appointment):
                await self._repositoryAppointment.save(appointment, command.scheduler_id)
                await self._bus.publish() #criar classe de evento
                return True
            
            
        except Exception as e:
            raise Exception("error ao criar Appointment", command)
      
    