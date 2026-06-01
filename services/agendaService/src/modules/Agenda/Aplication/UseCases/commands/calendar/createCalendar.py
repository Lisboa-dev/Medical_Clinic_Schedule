
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.externServices.CalendarDataPort import CalendarDataPort
from src.modules.agenda.aplication.ports.repository import RuleRepositoryPoty
from src.modules.agenda.aplication.ports.repository.CalendarRepositoryPort import CalendarRepositoryPort
from src.modules.agenda.domain.entities import Day


class CreateCalendarUseCase:
    
    def __init__(
        self, 
        repositoryCalendar: CalendarRepositoryPort, 
        repositoryRule: RuleRepositoryPoty,
        baseData: CalendarDataPort, 
        bus: BusPort
):
        
        self._repositoryCalendar = repositoryCalendar
        self._repositoryRule = repositoryRule
        self._baseData = baseData
        self_bus = bus


    async def execute(self, command: CreateCalendarCommand):
        try:
            data = await self._baseData.mont(command.day, command.ano)
            rules = await self._repositoryRule.getDayRules()
            
            if(data and rules):
                
                for d in data:
                    
                    try:
                        day = Day(**d)
                        day.addRules(rules)
                        await self._repository.save(day)
                    except:
                        await self._repository.delete(d['ano'])
                        raise Exception("error ao criar day", d)
                await self._bus.publish()
                return True
            
        except Exception as e:
            await self._repository.delete(command.ano)
            raise Exception("error ao criar day", command)
      
   
       
    