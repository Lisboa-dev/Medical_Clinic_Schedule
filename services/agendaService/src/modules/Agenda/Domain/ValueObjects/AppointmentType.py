from pydantic import BaseModel


class AppointmentType(BaseModel):
    name: str
    duration: int
    description: str