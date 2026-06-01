
from abc import ABC, abstractmethod

class RoomRepositoryPort(ABC):
    def save(self, room: Room)-> None:
       pass
   
    def update(self, room: Room)-> None:
       pass
   
    def delete(self, room_id: str)-> None:
       pass