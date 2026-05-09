from datetime import datetime

from src.Modules.Agenda.Domain.Entities.agendaClinicaEntity import BaseCalendarSlot
from src.Modules.Agenda.Domain.ValueObjects.slotStatus import SlotStatus


class Holiday:
    id: int

    clinic_id: int
 

    reason: str
    
    
    
class HolidayService:
    def apply(
        self,
        slots: list[BaseCalendarSlot],
        holidays: list[Holiday]
    ):

        for slot in slots:

            for holiday in holidays:

                overlap = (
                    slot.starts_at < holiday.ends_at
                    and
                    slot.ends_at > holiday.starts_at
                )

                if overlap:

                    slot.status = SlotStatus.HOLIDAY