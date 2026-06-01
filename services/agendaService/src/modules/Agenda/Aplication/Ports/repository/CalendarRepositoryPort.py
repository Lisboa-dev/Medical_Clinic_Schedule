
from abc import ABC, abstractmethod

from src.modules.agenda.domain.entities import Day
from ...services.Calendar import Calendar

class CalendarRepositoryPort (ABC):
   
   @abstractmethod
   def save(self, calendar:Calendar) ->  None:
       pass
   
   @abstractmethod
   def update(self, calendar:Calendar) -> None:
       pass
   
   @abstractmethod
   def delete(self) -> None:
       pass
   
   @abstractmethod
   def updateDay(self, day:Day) -> None:
       pass