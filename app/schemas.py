from pydantic import BaseModel, EmailStr
from typing import List, Optional

class InteractionBase(BaseModel):
    message: str
    response: str

class InteractionCreate(InteractionBase):
    pass

class InteractionResponse(InteractionBase):
    id: int
    class Config:
        orm_mode = True

class ClientBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class ClientResponse(ClientBase):
    id: int
    interactions: List[InteractionResponse] = []
    class Config:
        orm_mode = True
