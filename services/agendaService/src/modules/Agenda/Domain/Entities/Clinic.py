#abstração de um user admin que criará regras para a agenda, é importante que as policies sejam armazenadas aqui para manter a estrutura que o usuario criou
#isso pois as regras serão otimizadas para eliminar redundancias e facilitar os cálculos de agendamentos
from src.modules.agenda.domain.valueObjects.Id import ID

from ..rules.BaseRule import BaseRule





class Clinic:
    
    def __init__(
        self,
        rules: list[BaseRule],
        name: str,
        id: str = None,
    ):
        
        self._id = ID.generate_id() if id==None else ID(id)
        self._rules = rules
        self._name = name