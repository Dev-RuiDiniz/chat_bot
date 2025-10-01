from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Client
from ..schemas import ClientCreate, ClientResponse

router = APIRouter(prefix="/clients", tags=["Clients"])

@router.post("/", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.get("/", response_model=list[ClientResponse])
def list_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()

@router.get("/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    return db.query(Client).filter(Client.id == client_id).first()
