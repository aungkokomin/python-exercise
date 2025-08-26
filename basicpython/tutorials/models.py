from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int
    email: str
    active: bool= True
    created_at: datetime = datetime.now()

    def __init__(self, id: int, email: str, active: bool = True):
        self.id = id
        self.email = email
        self.active = active
        self.created_at = datetime.now()
    
    def activate(self) -> 'User':
        self.active = True
        return self
    def deactivate(self) -> 'User':
        self.active = False
        return self
        
        
    