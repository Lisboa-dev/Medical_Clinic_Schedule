from pydantic import BaseModel


class CreateAppointmentCommand(BaseModel):
    scheduler_id: str
    date:str
    weekday:str
    doctor:str
    patient:str
    time:str
    type:str
    
    
class DeleteAppointmentCommand(BaseModel):
    id: str
    
class UpdateAppointmentCommand(BaseModel):
    id: str