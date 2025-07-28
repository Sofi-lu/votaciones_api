from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.schemas import CandidateCreate, CandidateResponse
from typing import List
from models import Candidate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=CandidateResponse)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    db_candidate = Candidate(**candidate.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate


@router.get("/", response_model=list[CandidateResponse])
def list_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).all()


@router.get("/{candidate_id}", response_model=CandidateResponse)
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).get(candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato no encontrado.")
    return candidate


@router.delete("/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).get(candidate_id)
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato no encontrado.")
    db.delete(candidate)
    db.commit()
    return {"mensaje": "Candidato eliminado correctamente"}
