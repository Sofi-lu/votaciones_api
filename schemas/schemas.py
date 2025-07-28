from pydantic import BaseModel, EmailStr
from typing import Optional


# ---------------- VOTANTES ----------------
class VoterBase(BaseModel):
    name: str
    email: EmailStr

class VoterCreate(VoterBase):
    pass

class VoterResponse(VoterBase):
    id: int
    has_voted: bool

    class Config:
        from_attributes = True


# ---------------- CANDIDATOS ----------------
class CandidateBase(BaseModel):
    name: str
    party: str

class CandidateCreate(CandidateBase):
    pass

class CandidateResponse(CandidateBase):
    id: int
    votes_count: int  

    class Config:
        from_attributes = True


# ---------------- VOTOS ----------------
class VoteBase(BaseModel):
    voter_id: int
    candidate_id: int

class VoteCreate(VoteBase):
    pass

class VoteResponse(VoteBase):
    id: int

    class Config:
        from_attributes = True
