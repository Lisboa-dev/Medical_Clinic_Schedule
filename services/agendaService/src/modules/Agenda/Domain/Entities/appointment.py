from calendar import Day


from src.modules.agenda.domain.entities.Doctor import Doctor
from src.modules.agenda.domain.entities.Patient import Patient
from src.modules.agenda.domain.entities.Room import Room
from src.modules.agenda.domain.valueObjects import  Hour, RangeTime
from src.modules.agenda.domain.valueObjects.EnumAppointment import AppointmentStatus
from src.modules.agenda.domain.valueObjects.AppointmentType import  AppointmentType
from src.modules.agenda.domain.valueObjects.Id import ID




class Appointment:
   

    def __init__(
        self,
        rangeTime: RangeTime,
        patient: str,
        doctor: str,
        room: str,
        type: AppointmentType,
        time: Hour,
        status: AppointmentStatus,
        id: ID = None
    ) -> None:
        self._patient_id = patient
        self._doctor_id = doctor
        self._room_id = room
        self._type = type
        self._time = time
        self._status = status
        self._id = id
        self._rangeTime = rangeTime
        
      
    
    @staticmethod
    def create(
        patient: Patient,
        doctor: Doctor,
        room: list[Room],
        day: Day,
        time: Hour,
        type: AppointmentType,
    ):
        
        rangeTime = RangeTime.generate(time, type.duration)
        
        if(day.verifyInDisponibility(time) and doctor.verifyInDisponibility(time)): 
            
            roomSelected 
            for room in room:
                if(room.verifyInDisponibility(time)):
                    roomSelected = room
            
            if(roomSelected == None):
                return None
            
            return Appointment(
                id=ID(),
                patient=patient.id,
                doctor=doctor.id,
                room=roomSelected.id,
                time=time,
                type=type,
                status= AppointmentStatus.AVAILABLE,
                rangeTime=rangeTime
            )

        return None
       
    
    
    
    
    def verifyOverleaps(self, time):
        return self.time.overlaps(time)
    
    