class CreateAppointmentEvent:
    def __init__(self, patient: str, doctor: str, room: str, type: str, time: str):
        self.patient = patient
        self.doctor = doctor
        self.room = room
        self.type = type
        self.time = time
        

class UpdateAppointmentEvent:
    def __init__(self, id: str, patient: str, doctor: str, room: str, type: str, time: str):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.room = room
        self.type = type
        self.time = time
        
        
class DeleteAppointmentEvent:
    def __init__(self, id: str):
        self.id = id
        
        
        
class CancelAppointmentEvent:
    def __init__(self, id: str):
        self.id = id