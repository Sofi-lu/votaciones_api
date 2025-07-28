from fastapi import FastAPI
from database import Base, engine
from routers import voters, candidates, votes

app = FastAPI(title="Sistema de Votaciones")

Base.metadata.create_all(bind=engine)

app.include_router(voters.router, prefix="/voters", tags=["Voters"])
app.include_router(candidates.router, prefix="/candidates", tags=["Candidates"])
app.include_router(votes.router, prefix="/votes", tags=["Votes"])
