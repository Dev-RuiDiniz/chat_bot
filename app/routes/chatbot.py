from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import InteractionResponse
from models import Interaction
from services.chatbot_service import chatbot_response

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

@router.post("/interact", response_model=InteractionResponse)
def interact(client_id: int, message: str, db: Session = Depends(get_db)):
    response = chatbot_response(message)
    
    interaction = Interaction(client_id=client_id, message=message, response=response)
    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction
