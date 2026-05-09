import datetime

from src.Modules.Agenda.Domain.Entities.agendaClinicaEntity import BaseCalendarSlot
from src.Modules.Agenda.Domain.Entities.agendaMedicEntity import DoctorCalendarSlot
from src.Modules.Agenda.Domain.ValueObjects.slotStatus import SlotStatus


class Appointment:
    id: int

    patient_id: int
    doctor_id: int

    room_id: int

    doctor_slot_id: int
    base_slot_id: int

    starts_at: datetime
    ends_at: datetime
    

    def __init__(self, id: int, patient_id: int, doctor_id: int, room_id: int, doctor_slot_id: int, base_slot_id: int, starts_at: datetime, ends_at: datetime) -> None:
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.room_id = room_id
        self.doctor_slot_id = doctor_slot_id
        self.base_slot_id = base_slot_id
        self.starts_at = starts_at
        self.ends_at = ends_at
    
    
    @staticmethod
    def create(
        self,
        patient_id: int,
        doctor_slot: DoctorCalendarSlot,
        base_slot: BaseCalendarSlot
    ):

        if doctor_slot.status != SlotStatus.AVAILABLE:
            raise Exception("Doctor slot unavailable")

        if base_slot.status != SlotStatus.AVAILABLE:
            raise Exception("Room unavailable")

        doctor_slot.status = SlotStatus.BOOKED
        base_slot.status = SlotStatus.BOOKED

        appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_slot.doctor_id,
            room_id=base_slot.room_id,
            doctor_slot_id=doctor_slot.id,
            base_slot_id=base_slot.id,
            starts_at=doctor_slot.starts_at,
            ends_at=doctor_slot.ends_at
        )

        return appointment