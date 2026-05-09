
from datetime import datetime, timedelta
from src.Modules.Agenda.Domain.Policies.Clinic.clinicRule import ClinicRule
from src.Modules.Agenda.Domain.ValueObjects.slotData import SlotData
from src.Modules.Agenda.Domain.ValueObjects.slotStatus import SlotStatus


class BaseCalendarGenerator:

    def generate(
        self,
        clinic_rule: ClinicRule,
        room_id: int,
        base_date: datetime
    ):

        slots = [SlotData]

        current = datetime.combine(
            base_date.date(),
            datetime.strptime(
                clinic_rule.starts_at,
                "%H:%M"
            ).time()
        )

        end = datetime.combine(
            base_date.date(),
            datetime.strptime(
                clinic_rule.ends_at,
                "%H:%M"
            ).time()
        )

        while current < end:

            slot_end = current + timedelta(
                minutes=clinic_rule.slot_duration_minutes
            )

            slots.append(
                BaseCalendarSlot(
                    room_id=room_id,
                    starts_at=current,
                    ends_at=slot_end,
                    status=SlotStatus.AVAILABLE
                )
            )

            current = slot_end

        return slots
    
   
    
    
    
