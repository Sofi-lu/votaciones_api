from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.VoterResponse)
def create_voter(voter: schemas.VoterCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Voter).filter(models.Voter.email == voter.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Correo ya registrado.")
    db_voter = models.Voter(**voter.dict())
    db.add(db_voter)
    db.commit()
    db.refresh(db_voter)
    return db_voter


@router.get("/", response_model=list[schemas.VoterResponse])
def list_voters(db: Session = Depends(get_db)):
    return db.query(models.Voter).all()


@router.get("/{voter_id}", response_model=schemas.VoterResponse)
def get_voter(voter_id: int, db: Session = Depends(get_db)):
    voter = db.query(models.Voter).get(voter_id)
    if not voter:
        raise HTTPException(status_code=404, detail="Votante no encontrado.")
    return voter


@router.delete("/{voter_id}")
def delete_voter(voter_id: int, db: Session = Depends(get_db)):
    voter = db.query(models.Voter).get(voter_id)
    if not voter:
        raise HTTPException(status_code=404, detail="Votante no encontrado.")
    db.delete(voter)
    db.commit()
    return {"mensaje": "Votante eliminado correctamente"}
