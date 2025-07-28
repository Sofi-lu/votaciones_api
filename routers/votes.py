from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.schemas import VoteCreate, VoteResponse
from models import Voter, Candidate, Vote
from utils.auth import verify_credentials


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=VoteResponse)
def cast_vote(vote: VoteCreate, db: Session = Depends(get_db),username: str = Depends(verify_credentials)):
    voter = db.query(Voter).get(vote.voter_id)
    candidate = db.query(Candidate).get(vote.candidate_id)

    if not voter or not candidate:
        raise HTTPException(status_code=404, detail="Votante o candidato no encontrado.")

    if voter.has_voted:
        raise HTTPException(status_code=400, detail="Este votante ya ha votado.")

    db_vote = Vote(voter_id=vote.voter_id, candidate_id=vote.candidate_id)
    db.add(db_vote)

    voter.has_voted = True
    candidate.votes_count += 1

    db.commit()
    db.refresh(db_vote)
    return db_vote


@router.get("/", response_model=list[VoteResponse])
def list_votes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Vote).offset(skip).limit(limit).all()



@router.get("/statistics")
def vote_statistics(db: Session = Depends(get_db)):
    candidates = db.query(Candidate).all()
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

    total_voters = db.query(Voter).count()
    voters_who_voted = db.query(Voter).filter(Voter.has_voted == True).count()

    return {
        "total_votes": total_votes,
        "total_voters": total_voters,
        "voters_who_voted": voters_who_voted,
        "results": stats
    }
