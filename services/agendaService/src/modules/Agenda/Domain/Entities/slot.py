
from dataclasses import dataclass
from typing import Optional


from sqlalchemy import Date
from src.Modules.Agenda.Domain.ValueObjects.rangeTime import RangeTime
from src.Modules.Agenda.Domain.ValueObjects.slotStatus import SlotStatus


class Slot:
    id: int
    appointmentList_id: list[int]
    room_id: int
    date:Date
    weekday:int
    availability: int
    status: SlotStatus
    hoursExceptions: Optional[list[RangeTime]] 
    
    def __init__(
        self,
        room_id: int,
        date: Date,
        weekday: int,
        slot_id: int,
        availability: int,
        status: SlotStatus,
        hoursRange: list[RangeTime],
        appointmentList_id:list[int]=[],
        hoursExceptions: list[RangeTime] = None
        
    ):

        self.room_id = room_id
        self.date = date
        self.availability = availability
        self.weekday = weekday
        self.status = status
        self.appointmentList_id = appointmentList_id
        self.id = slot_id
        self.hoursRange = hoursRange
        self.hoursExceptions = hoursExceptions
        
    
    def updateState(self, newStatus: SlotStatus):
        self.status = newStatus