class ClinicRuleGeneric:
    id: int

    clinic_id: int

    weekday: int

    starts_at: str
    ends_at: str

    slot_duration_minutes: int
    


class ClinicRuleException:
    id: int

    clinic_id: int

    weekday: int

    starts_at: str
    ends_at: str

    slot_duration_minutes: int