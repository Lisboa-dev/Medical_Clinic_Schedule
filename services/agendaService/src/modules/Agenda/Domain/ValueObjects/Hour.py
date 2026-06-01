
from datetime import datetime



class Hour:
    TIME_PATTERN = "%H:%M"
     
    def __init__(self) -> None:
        self.hour = datetime.now().strftime(self.TIME_PATTERN)
        
    
    def compare(self, hour: str) -> bool:
        return self.hour == hour
