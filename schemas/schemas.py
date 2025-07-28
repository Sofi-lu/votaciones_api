from pydantic import BaseModel, EmailStr
from typing import Optional

class VoterBase(BaseModel):
    name: str
    email: EmailStr

class VoterCreate(VoterBase):
    pass

class VoterResponse(VoterBase):
    id: int
    has_voted: bool
    class Config:
        orm_mode = True

class CandidateBase(BaseModel):
    name: str
    party: Optional[str] = None

class CandidateCreate(CandidateBase):
    pass

class CandidateResponse(CandidateBase):
    id: int
    votes_count: int
    class Config:
        orm_mode = True

class VoteCreate(BaseModel):
    voter_id: int
    candidate_id: int

class VoteResponse(BaseModel):
    id: int
    voter_id: int
    candidate_id: int
    class Config:
        orm_mode = True
