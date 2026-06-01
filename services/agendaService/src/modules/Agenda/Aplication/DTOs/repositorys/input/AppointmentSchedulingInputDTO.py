from pydantic import BaseModel


class AppointmentSchedulingInputDTO(BaseModel):
        patient: str
        doctor: str
        room: str
        type: str
        time: str
        date: str
        weekday: str
      
     