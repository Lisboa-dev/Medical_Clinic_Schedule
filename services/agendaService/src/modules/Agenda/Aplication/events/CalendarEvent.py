class CreateCalendarEvents:
    def __init__(self, repository: CalendarRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    
    
class CreateCalendarEvent:
    def __init__(self, doctor: str, date: str):
        self.doctor = doctor
        self.date = date
        
        
        
class DeleteCalendarEvent:
    def __init__(self, doctor: str, date: str):
        self.doctor = doctor
        self.date = date