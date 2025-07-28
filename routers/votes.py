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


@router.post("/", response_model=schemas.VoteResponse)
def cast_vote(vote: schemas.VoteCreate, db: Session = Depends(get_db)):
    voter = db.query(models.Voter).get(vote.voter_id)
    candidate = db.query(models.Candidate).get(vote.candidate_id)

    if not voter or not candidate:
        raise HTTPException(status_code=404, detail="Votante o candidato no encontrado.")

    if voter.has_voted:
        raise HTTPException(status_code=400, detail="Este votante ya ha votado.")

    db_vote = models.Vote(voter_id=vote.voter_id, candidate_id=vote.candidate_id)
    db.add(db_vote)

    voter.has_voted = True
    candidate.votes_count += 1

    db.commit()
    db.refresh(db_vote)
    return db_vote


@router.get("/", response_model=list[schemas.VoteResponse])
def list_votes(db: Session = Depends(get_db)):
    return db.query(models.Vote).all()


@router.get("/statistics")
def vote_statistics(db: Session = Depends(get_db)):
    candidates = db.query(models.Candidate).all()
    total_votes = sum(c.votes_count for c in candidates)
    stats = []

    for c in candidates:
        percent = (c.votes_count / total_votes) * 100 if total_votes else 0
        stats.append({
            "candidate": c.name,
            "party": c.party,
            "votes": c.votes_count,
            "percentage": round(percent, 2)
        })

    total_voters = db.query(models.Voter).count()
    voters_who_voted = db.query(models.Voter).filter(models.Voter.has_voted == True).count()

    return {
        "total_votes": total_votes,
        "total_voters": total_voters,
        "voters_who_voted": voters_who_voted,
        "results": stats
    }
