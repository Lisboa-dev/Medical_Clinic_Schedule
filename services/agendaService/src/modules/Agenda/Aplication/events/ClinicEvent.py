class CreateClinicEvent:
    def __init__(self, name: str, address: str, phone: str):
        self.name = name
        self.address = address
        self.phone = phone
        
        
class UpdateClinicEvent:
    def __init__(self, id: str, name: str, address: str, phone: str):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        
        
        
class DeleteClinicEvent:
    def __init__(self, id: str):
        self.id = id