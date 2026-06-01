
from src.modules.agenda.aplication.dtos.useCase.command.RoomUseCasesDTO import UpdateRoomCommand
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository.RoomRepositoryPort import RoomRepositoryPort


class UpdateRoom:
    def __init__(self, repository: RoomRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus= bus
    
    def execute(self, Imput:UpdateRoomCommand) -> bool:
         room = self._repository.getRoom(Imput.id_room)
         roomUpdated = room.updateStateRoom(Imput)
         
         if(roomUpdated and self._repository.update(roomUpdated)):
             return True
         
         return False