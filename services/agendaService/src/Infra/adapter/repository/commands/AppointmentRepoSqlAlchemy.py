
from src.modules.agenda.aplication.ports.repository.AppointmentRepositoryPort import AppointmentRepositoryPort


class AppointmentRepository(AppointmentRepositoryPort):
    def __init__(self):
        self.appointments = []
        self.counter = 1