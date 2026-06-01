from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.domain.entities.Room import Room
from src.modules.agenda.aplication.ports.repository.RoomRepositoryPort import RoomRepositoryPort

class DeleteRoom:
    def __init__(self, repository: RoomRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus= bus
    def execute(self, room_id: int) -> bool:
        try:
            room =self._repository.getRoom(room_id) 
            roomEntity = Room(name = room.name, disponibility = room.disponibility, rules = room.rules)
            
            if(room and roomEntity.delete()):
                self._repository.deleteRoom(room_id)
                self._bus.emit('roomDeleted', room_id)
                return True
        
        except Exception as e:
            return 
       