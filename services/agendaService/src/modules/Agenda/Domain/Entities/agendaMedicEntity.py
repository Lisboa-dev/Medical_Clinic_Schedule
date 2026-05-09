import datetime
from src.Modules.Agenda.Domain.Entities.agendaClinicaEntity import BaseCalendarSlot
from src.Modules.Agenda.Domain.Entities.docttor import Doctor
from src.Modules.Agenda.Domain.ValueObjects.slotStatus import SlotStatus


class DoctorCalendarSlot:
    id: int

    doctor_id: int

    base_slot_id: int

    starts_at: datetime
    ends_at: datetime

    status: SlotStatus
    
    
    

class DoctorAvailability:
    id: int

    doctor_id: int

    weekday: int

    starts_at: str
    ends_at: str
    


class DoctorCalendarGenerator:

    def generate(
        self,
        doctor: Doctor,
        availability: DoctorAvailability,
        base_slots: list[BaseCalendarSlot]
    ):

        doctor_slots = []

        for slot in base_slots:

            start_time = slot.starts_at.time()

            availability_start = datetime.strptime(
                availability.starts_at,
                "%H:%M"
            ).time()

            availability_end = datetime.strptime(
                availability.ends_at,
                "%H:%M"
            ).time()

            if availability_start <= start_time < availability_end:

                doctor_slots.append(
                    DoctorCalendarSlot(
                        doctor_id=doctor.id,
                        base_slot_id=slot.id,
                        starts_at=slot.starts_at,
                        ends_at=slot.ends_at,
                        status=SlotStatus.AVAILABLE
                    )
                )

        return doctor_slots
    
    