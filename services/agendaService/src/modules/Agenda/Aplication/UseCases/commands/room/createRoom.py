from src.Modules.Agenda.Domain.Entities.room import Room
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository.RoomRepositoryPort import RoomRepositoryPort


class CreateRoomUseCase:
    def __init__(self, repository: RoomRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, name: str) -> bool:
        try:
            rules=await self._repository.getGenericRulesRoom()
            room = Room(name=name, rules=rules)
            if isinstance(room,Room):
             await self._repository.save(room) 
             return True
        
        except Exception as e:
            return Exception("error ao criar ", e)